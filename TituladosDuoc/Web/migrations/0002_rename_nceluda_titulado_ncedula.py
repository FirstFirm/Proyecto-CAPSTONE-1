# Generated by Django 4.2.1 on 2023-10-23 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titulado',
            old_name='NCeluda',
            new_name='NCedula',
        ),
    ]