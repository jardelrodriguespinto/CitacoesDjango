# Generated by Django 2.2.12 on 2022-10-30 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citacoesapp', '0002_citacoes_data_da_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citacoes',
            name='data_da_publicacao',
        ),
    ]
