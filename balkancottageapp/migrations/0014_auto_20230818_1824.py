# Generated by Django 3.2.18 on 2023-08-18 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balkancottageapp', '0013_alter_reservation_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
    ]
