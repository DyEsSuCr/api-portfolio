# Generated by Django 4.1.5 on 2023-01-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
