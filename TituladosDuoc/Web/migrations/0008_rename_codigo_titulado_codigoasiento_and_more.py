# Generated by Django 4.2.6 on 2023-10-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0007_alter_titulado_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titulado',
            old_name='Codigo',
            new_name='CodigoAsiento',
        ),
        migrations.RemoveField(
            model_name='titulado',
            name='Celular',
        ),
        migrations.RemoveField(
            model_name='titulado',
            name='Email',
        ),
    ]
