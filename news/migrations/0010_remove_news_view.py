# Generated by Django 3.0.6 on 2020-07-24 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_news_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view',
        ),
    ]
