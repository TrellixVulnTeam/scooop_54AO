# Generated by Django 3.0.6 on 2020-07-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200712_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.TextField(default=''),
        ),
    ]
