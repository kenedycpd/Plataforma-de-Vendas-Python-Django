# Generated by Django 2.0 on 2018-09-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0015_auto_20180921_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidovenda',
            name='preco_compra',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Preço do Produto'),
        ),
    ]
