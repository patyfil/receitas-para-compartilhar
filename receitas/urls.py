from django.urls import path, reverse_lazy
from receitas import views
from django.contrib.auth import views as auth_views

app_name = 'receitas'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),

    # login
    path('login/', views.loginUser, name="loginUser"),
    # Logout
    path('logout/', views.logoutUser, name="logoutUser"),

    # User cadastro
    path('cadastroUser/', views.cadastroUser, name="cadastroUser"),

    # Redefinir senha
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='receitas/reset_password_form.html',
        email_template_name='receitas/reset_password_email.html',
        success_url=reverse_lazy('receitas:password_reset_done')
    ), name='password_reset'),

    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='receitas/reset_password_done.html'
    ), name='password_reset_done'),


    # CRUD RECEITA
    path('receita/<int:receitaId>/detail/', views.receita, name='receita'),
    path('receita/create', views.createReceita, name='createReceita'),
    path('receita/<int:receitaId>/update/',
         views.updateReceita, name='updateReceita'),
    path('receita/<int:receitaId>/delete/',
         views.deleteReceita, name='deleteReceita'),
]
