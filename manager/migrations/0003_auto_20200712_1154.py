# Generated by Django 3.0.6 on 2020-07-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.CharField(default='@gmail.com', max_length=40),
        ),
    ]
