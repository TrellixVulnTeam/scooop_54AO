# Generated by Django 3.0.6 on 2020-07-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200723_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='aboutus',
            field=models.TextField(default=''),
        ),
    ]
