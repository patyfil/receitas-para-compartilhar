# Generated by Django 4.2.7 on 2023-11-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_alter_receita_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='imagem',
            field=models.ImageField(upload_to='receitas/'),
        ),
    ]
