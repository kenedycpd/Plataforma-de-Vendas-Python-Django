# Generated by Django 2.0 on 2018-08-31 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_pedidovenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastroproduto',
            name='codigo',
        ),
    ]
