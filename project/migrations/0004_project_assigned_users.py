# Generated by Django 5.0.6 on 2024-06-25 06:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_title_project_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assigned_users',
            field=models.ManyToManyField(related_name='assigned_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]