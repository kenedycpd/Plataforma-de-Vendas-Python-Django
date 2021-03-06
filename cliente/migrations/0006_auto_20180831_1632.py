# Generated by Django 2.0 on 2018-08-31 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20180831_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidovenda',
            name='quantidade',
            field=models.CharField(default=1, max_length=10, verbose_name='Quantidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.CadastroProduto'),
        ),
    ]
