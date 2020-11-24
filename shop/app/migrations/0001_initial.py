# Generated by Django 2.2.1 on 2020-11-01 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Tên')),
                ('code', models.CharField(max_length=200, verbose_name='Mã')),
                ('diameter', models.FloatField(verbose_name='Đường kính mặt đồng hồ (mm)')),
                ('diameter_face', models.CharField(max_length=250, verbose_name='Chất liệu mặt')),
                ('material_albert', models.CharField(max_length=20, verbose_name='Chất liệu dây')),
                ('material_case', models.CharField(max_length=50, verbose_name='Chất liệu vỏ')),
                ('price', models.IntegerField(verbose_name='Giá (đ)')),
                ('image', models.ImageField(upload_to='statics/images', verbose_name='Ảnh sản phẩm')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Manufacturer', verbose_name='Hãng Sản Xuất')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('priceUnit', models.FloatField()),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('dateOrder', models.DateTimeField()),
                ('deliverDate', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Product')),
            ],
        ),
    ]