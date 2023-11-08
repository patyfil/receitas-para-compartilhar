# CÓDIGO PARA EXCLUIR IMAGENS DE RECEITAS EXCLUIDAS

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage

from receitas import models


@receiver(pre_delete, sender=models.Receita)
def delete_receita_images(sender, instance, **kwargs):
    # Verifique se a instância tem uma imagem
    if instance.imagem:
        # Construa o caminho do arquivo da imagem
        image_path = instance.imagem.path
        # Exclua o arquivo de imagem da pasta de mídia
        default_storage.delete(image_path)
