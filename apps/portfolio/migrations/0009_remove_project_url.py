# Generated by Django 4.1.5 on 2023-01-13 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_demo_alter_project_github'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]
