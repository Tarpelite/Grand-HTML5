# Generated by Django 2.0.5 on 2018-06-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20180605_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='Number',
        ),
    ]
