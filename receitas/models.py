from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ImageField(upload_to='receitas/')
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()

    def __str__(self):
        return self.titulo
