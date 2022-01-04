# Generated by Django 4.0 on 2022-01-03 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.IntegerField()),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]