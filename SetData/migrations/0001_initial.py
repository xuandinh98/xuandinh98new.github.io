# Generated by Django 3.2.7 on 2021-09-30 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('STT', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_id', models.CharField(max_length=10)),
                ('category_name', models.TextField()),
                ('category_parent_id', models.IntegerField()),
                ('category_slug', models.CharField(max_length=255)),
                ('category_status', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TickerCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_code_id', models.IntegerField(default=1)),
                ('category', models.CharField(max_length=5)),
                ('product', models.CharField(max_length=5)),
                ('service', models.CharField(max_length=5)),
                ('unit', models.CharField(max_length=5)),
                ('vendor', models.CharField(max_length=5)),
                ('partner', models.CharField(max_length=5)),
                ('user', models.CharField(max_length=5)),
                ('customer', models.CharField(max_length=5)),
                ('order', models.CharField(max_length=5)),
                ('invoice', models.CharField(max_length=5)),
                ('goods_received_note', models.CharField(max_length=5)),
                ('goods_delivery_note', models.CharField(max_length=5)),
                ('inventory_sheet', models.CharField(max_length=5)),
                ('shipping_unit', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('STT', models.BigAutoField(primary_key=True, serialize=False)),
                ('unit_id', models.CharField(max_length=10)),
                ('unit_name', models.TextField()),
                ('unit_slug', models.CharField(max_length=255)),
                ('category_status', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]