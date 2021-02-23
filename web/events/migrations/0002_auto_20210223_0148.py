# Generated by Django 3.0 on 2021-02-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
