# Generated by Django 4.0 on 2021-12-24 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_location_hood_host_post_alter_hood_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hood',
            name='location',
        ),
    ]