# Generated by Django 2.0.5 on 2018-06-05 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_remove_homework_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='Student',
        ),
    ]
