# Generated by Django 3.0.6 on 2020-07-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200605_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fblink',
            field=models.CharField(default='#', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='tel',
            field=models.CharField(default='987654321', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='twlink',
            field=models.CharField(default='#', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='ytlink',
            field=models.CharField(default='#', max_length=30),
        ),
    ]
