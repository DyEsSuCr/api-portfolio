# Generated by Django 4.1.5 on 2023-01-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(max_length=120, verbose_name='Descripción')),
                ('image', models.ImageField(default='photo-default.png', upload_to='img_projects/', verbose_name='Imagen')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-title'],
            },
        ),
    ]
