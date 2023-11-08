from django.apps import AppConfig


class ReceitasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'receitas'

    def ready(self):
        import receitas.signals  # Importa o arquivo signals.py
