# Generated by Django 3.2.3 on 2021-05-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_app', '0003_auto_20210523_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='news1'),
            preserve_default=False,
        ),
    ]
