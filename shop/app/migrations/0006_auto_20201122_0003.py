# Generated by Django 3.1 on 2020-11-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201120_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material_albert',
            field=models.CharField(max_length=100, verbose_name='Chất liệu dây'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material_case',
            field=models.CharField(max_length=100, verbose_name='Chất liệu vỏ'),
        ),
    ]
