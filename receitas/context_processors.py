from .models import Categoria


def menu_items(request):
    categorias = Categoria.objects.all()
    menu_items = [
        {'text': 'Todas as receitas', 'query': ''},
    ]

    for categoria in categorias:
        menu_items.append({'text': categoria.nome, 'query': categoria.nome})

    return {'menu_items': menu_items}
