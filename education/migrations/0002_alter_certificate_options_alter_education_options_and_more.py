# Generated by Django 4.0.1 on 2022-01-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['-date'], 'verbose_name': 'Certificado formativo', 'verbose_name_plural': 'Certificados formativos'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-date'], 'verbose_name': 'Formación reglada', 'verbose_name_plural': 'Formaciones regladas'},
        ),
        migrations.AlterField(
            model_name='certificate',
            name='link',
            field=models.URLField(blank=True, verbose_name='Enlace'),
        ),
    ]
