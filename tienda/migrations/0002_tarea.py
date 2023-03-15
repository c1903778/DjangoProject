# Generated by Django 4.1.2 on 2022-10-22 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.proyecto')),
            ],
        ),
    ]