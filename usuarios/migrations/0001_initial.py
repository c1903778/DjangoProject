# Generated by Django 4.1.2 on 2023-02-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=12)),
                ('pais', models.CharField(max_length=30)),
            ],
        ),
    ]