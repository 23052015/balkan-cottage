# Generated by Django 3.2.18 on 2023-08-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balkancottageapp', '0011_remove_reservation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='message',
            field=models.TextField(default=0, max_length=300),
        ),
    ]
