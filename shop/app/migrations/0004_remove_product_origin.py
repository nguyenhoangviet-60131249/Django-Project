# Generated by Django 3.1 on 2020-11-19 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201118_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='origin',
        ),
    ]
