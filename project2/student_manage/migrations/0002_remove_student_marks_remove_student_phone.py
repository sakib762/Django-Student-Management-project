# Generated by Django 5.1.5 on 2025-02-02 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_manage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]
