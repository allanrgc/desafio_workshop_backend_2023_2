# Generated by Django 4.2.4 on 2023-09-05 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_carrinho_total_alter_produto_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='itens',
        ),
    ]
