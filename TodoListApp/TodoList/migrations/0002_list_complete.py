# Generated by Django 5.0.1 on 2024-01-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
