from django.contrib import admin
from . import models


@admin.register(models.Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'titulo', 'categoria', 'subtitulo', 'ingredientes', 'modo_preparo'
    )
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10



@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...