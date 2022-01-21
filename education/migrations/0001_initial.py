# Generated by Django 4.0.1 on 2022-01-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('center', models.CharField(max_length=150, verbose_name='Centro')),
                ('logo', models.ImageField(upload_to='centro/', verbose_name='Logotipo')),
                ('date', models.DateField(verbose_name='Fecha de finalización')),
                ('link', models.URLField(verbose_name='Enlace')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('center', models.CharField(max_length=150, verbose_name='Centro')),
                ('logo', models.ImageField(upload_to='centro/', verbose_name='Logotipo')),
                ('date', models.DateField(verbose_name='Fecha de finalización')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
    ]
