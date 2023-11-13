from django.shortcuts import render, redirect, get_object_or_404

from receitas.context_processors import menu_items
from . import models
# from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages import constants

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


# Página inicial


def index(request):
    receitas = models.Receita.objects.all()

    paginator = Paginator(receitas, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Chame a função menu_items para obter a lista de itens do menu (arquivo context_processors.py)
    menu_data = menu_items(request)

    context = {
        'page_obj': page_obj,
        # Use a lista de itens do menu do contexto
        'menuItems': menu_data['menu_items'],
        'current_query': request.GET.get('q', ''),
    }

    return render(request, 'receitas/index.html', context)


# Visualização de uma receita específica

def receita(request, receitaId):
    receita_unica = get_object_or_404(models.Receita, id=receitaId)
    ingredientes = textFormater(receitaId, tipo='ingredientes')
    modo_preparo = textFormater(receitaId, tipo='modo_preparo')
    
    print(f"User: {request.user}")
    print(f"Receita Usuario: {receita_unica.usuario}")
    receita_usuario = getattr(receita_unica, 'usuario', None)

    context = {
        'receita': receita_unica,
        'ingredientes': ingredientes,
        'modo_preparo': modo_preparo,
        'user': request.user, 
        'receita_usuario': receita_usuario,
    }
    return render(request, 'receitas/receita.html', context)


# Criação de uma nova receita

@login_required
def createReceita(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário POST
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        ingredientes = request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')
        imagem = request.FILES.get('imagem')
        categoria_nome = request.POST.get('categoria')

        # Verifique se a categoria existe
        try:
            categoria = models.Categoria.objects.get(nome=categoria_nome)
        except models.Categoria.DoesNotExist:
            messages.error(request, 'A categoria especificada não existe.')
            return redirect('receitas:cadastro')

        if imagem:
            # Crie uma nova instância de Receita e salve no banco de dados
            nova_receita = models.Receita(
                titulo=titulo,
                subtitulo=subtitulo,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo,
                imagem=imagem,
                categoria=categoria,
                usuario=request.user  # Adicione esta linha para associar o usuário à receita
            )
            nova_receita.save()

            # Salve a mensagem de sucesso na sessão do usuário
            messages.add_message(request, constants.SUCCESS, "Receita criada com sucesso.")

            # Redirecione para a página inicial após a criação
            return redirect('receitas:createReceita')

        else:
            messages.error(request, 'Erro ao fazer o upload da imagem')

    # Exiba o formulário de criação de receita vazio
    categorias = models.Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'receitas/cadastro.html', context)


# Atualização de uma receita existente

@login_required
def updateReceita(request, receitaId):
    receita = get_object_or_404(models.Receita, id=receitaId)
    categorias = models.Categoria.objects.all()

    # Verifique se o usuário logado é o criador da receita
    if request.user != receita.usuario:
        return HttpResponseForbidden("Você não tem permissão para editar esta receita.")

    if request.method == 'POST':
        receita.titulo = request.POST.get('titulo')
        receita.subtitulo = request.POST.get('subtitulo')
        receita.ingredientes = request.POST.get('ingredientes')
        receita.modo_preparo = request.POST.get('modo_preparo')

        if 'imagem' in request.FILES:
            receita.imagem = request.FILES['imagem']

        # Obter o nome da categoria selecionada no formulário
        categoria_id = request.POST.get('categoria')

        try:
            categoria = models.Categoria.objects.get(id=categoria_id)
            receita.categoria = categoria
            receita.save()
            return redirect('receitas:index')
        except models.Categoria.DoesNotExist:
            pass

    # Exibir o formulário de atualização de receita preenchido com os dados atuais
    context = {
        'receita': receita,
        'categorias': categorias,
    }
    return render(request, 'receitas/editarReceita.html', context)


# Exclusão de uma receita


@login_required
def deleteReceita(request, receitaId):
    receita = get_object_or_404(
        models.Receita, id=receitaId)

    # Verifique se o usuário logado é o criador da receita
    if request.user != receita.usuario:
        return HttpResponseForbidden("Você não tem permissão para excluir esta receita.")

    # Remova a receita do banco de dados
    receita.delete()
    messages.success(request, 'Receita excluída com sucesso.')

    return redirect('receitas:index')
    # Limpe as mensagens após a exibição
    messages.get_messages(request).used = True



...

# Pesquisa de receitas


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('receitas:index')

    receitas = models.Receita.objects.filter(
        Q(titulo__icontains=search_value) | Q(subtitulo__icontains=search_value) | Q(
            ingredientes__icontains=search_value) | Q(categoria__nome__icontains=search_value))

    # Chame a função menu_items para obter a lista de itens do menu
    menu_data = menu_items(request)

    paginator = Paginator(receitas, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_value': search_value,
        # Use a lista de itens do menu do contexto
        'menuItems': menu_data['menu_items'],
        'current_query': search_value,  # Defina o valor de current_query como a busca
    }

    return render(request, 'receitas/index.html', context)

# Página de login


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # messages.add_message(request, constants.SUCCESS, "Logado com sucesso")
            return redirect('receitas:index')
        else:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos')
            return redirect('receitas:loginUser')
    return render(request, 'receitas/login.html')

# Página de logout


@login_required
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)

        messages.add_message(request, constants.SUCCESS, 'Você saiu!')
    return redirect('receitas:loginUser')


# Página de cadastro de usuário
# Função para criar um usuário


def criar_usuario(username, email, password):
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return user
    except Exception as e:
        print(f"Erro ao criar usuário: {str(e)}")

        return None

# Função para cadastrar um usuário


def cadastroUser(request):
    if request.method == 'GET':
        return render(request, 'receitas/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if not password == confirmPassword:
            messages.add_message(request, constants.ERROR,
                                 "As senhas não são iguais")
            return redirect('receitas:cadastroUser')

        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR,
                                 'Nome de usuário já existe')
            return redirect('receitas:cadastroUser')

        user = criar_usuario(username, email, password)
        if user is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.add_message(request, constants.SUCCESS, 'Conta criada e logada com sucesso')
                return redirect('receitas:index')
        else:
            messages.add_message(request, constants.ERROR,
                                 'Erro ao criar conta')
            return redirect('receitas:cadastroUser')


# Formatação de texto

def textFormater(id, tipo):
    if tipo == 'ingredientes':
        receita = models.Receita.objects.get(id=id)
        ing = receita.ingredientes
        lista = ing.split('\n')
        return lista
    elif tipo == 'modo_preparo':
        modo_preparo = models.Receita.objects.get(id=id).modo_preparo
        lista = modo_preparo.split('\n')
        return lista


def reset_password(request):
    return PasswordResetView.as_view(
        template_name='receitas/reset_password_form.html',
        email_template_name='receitas/reset_password_email.html',
        success_url=reverse_lazy('receitas:password_reset_done')
    )(request)


def password_reset_done(request):
    return PasswordResetDoneView.as_view(template_name='receitas/reset_password_done.html')(request)


def password_reset_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name='receitas/reset_password_confirm.html',
        success_url=reverse_lazy('receitas:password_reset_complete')
    )(request, uidb64=uidb64, token=token)


def password_reset_complete(request):
    return PasswordResetCompleteView.as_view(template_name='receitas/reset_password_complete.html')(request)
