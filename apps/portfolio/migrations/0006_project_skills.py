# Generated by Django 4.1.5 on 2023-01-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_skill_icon'),
        ('portfolio', '0005_alter_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='skills.skill'),
        ),
    ]
