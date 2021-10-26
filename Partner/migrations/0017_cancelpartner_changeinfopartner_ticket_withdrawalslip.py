# Generated by Django 3.2.7 on 2021-10-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partner', '0016_auto_20211017_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelPartner',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.IntegerField()),
                ('partner_id', models.IntegerField()),
                ('date_cancel', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChangeInfoPartner',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.IntegerField()),
                ('partner_id', models.IntegerField()),
                ('partner_firstname', models.TextField()),
                ('partner_lastname', models.TextField(null=True)),
                ('partner_sex', models.IntegerField(null=True)),
                ('partner_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('store_name', models.TextField()),
                ('store_image', models.ImageField(blank=True, upload_to='')),
                ('partner_phone', models.CharField(max_length=11)),
                ('partner_phone2', models.CharField(max_length=11)),
                ('partner_birthday', models.DateField()),
                ('partner_email', models.TextField()),
                ('partner_address', models.TextField()),
                ('partner_area', models.TextField()),
                ('partner_province', models.TextField()),
                ('partner_district', models.TextField()),
                ('partner_wards', models.TextField()),
                ('police_certificate', models.FileField(blank=True, upload_to='')),
                ('partner_bank_account', models.TextField()),
                ('bank_name', models.TextField()),
                ('bank_account_holder_name', models.CharField(max_length=255)),
                ('bank_branch', models.TextField(null=True)),
                ('typerepair_xedap', models.IntegerField(null=True)),
                ('typerepair_xemay', models.IntegerField(null=True)),
                ('typerepair_xehoi', models.IntegerField(null=True)),
                ('typerepair_xekeo', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partner_id', models.IntegerField()),
                ('desc', models.TextField()),
                ('status', models.IntegerField()),
                ('confirm_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalSlip',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.IntegerField()),
                ('money_withdraw', models.IntegerField()),
                ('bank', models.TextField()),
                ('bank_account', models.TextField()),
                ('bank_owner', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
