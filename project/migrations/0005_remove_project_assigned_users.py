# Generated by Django 5.0.6 on 2024-06-30 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_assigned_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assigned_users',
        ),
    ]
