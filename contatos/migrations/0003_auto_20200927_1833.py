# Generated by Django 3.1.1 on 2020-09-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_exibicao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='exibicao',
            new_name='mostrar',
        ),
    ]