# Generated by Django 3.2.18 on 2023-04-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balkancottageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
