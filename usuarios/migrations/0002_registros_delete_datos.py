# Generated by Django 4.1.2 on 2023-03-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=12)),
                ('pais', models.CharField(max_length=30)),
                ('cuidad', models.CharField(max_length=30)),
                ('postal', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='datos',
        ),
    ]
