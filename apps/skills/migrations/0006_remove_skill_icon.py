# Generated by Django 4.1.5 on 2023-01-13 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_skill_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icon',
        ),
    ]
