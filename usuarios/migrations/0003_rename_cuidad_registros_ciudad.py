# Generated by Django 4.1.2 on 2023-03-12 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_registros_delete_datos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registros',
            old_name='cuidad',
            new_name='ciudad',
        ),
    ]
