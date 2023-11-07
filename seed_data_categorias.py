from receitas.models import Categoria
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def seed_data_categorias():
    # Cria as categorias
    Categoria.objects.create(nome='Sobremesas')
    Categoria.objects.create(nome='Sopas')
    Categoria.objects.create(nome='Grelhados')
    Categoria.objects.create(nome='Aperitivos')
    Categoria.objects.create(nome='Massas')
    Categoria.objects.create(nome='Saladas')


seed_data_categorias()
