# Generated by Django 2.0 on 2018-09-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_pedidovenda_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidovenda',
            name='total',
        ),
    ]
