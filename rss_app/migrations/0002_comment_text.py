# Generated by Django 3.2.3 on 2021-05-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
