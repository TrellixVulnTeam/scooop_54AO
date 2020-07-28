# Generated by Django 3.0.6 on 2020-06-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='news',
            name='view',
            field=models.CharField(default='-', max_length=1000),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='news',
            name='headline',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
