# Generated by Django 4.0 on 2021-12-24 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_hood_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]
