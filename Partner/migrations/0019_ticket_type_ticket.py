# Generated by Django 3.2.7 on 2021-10-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partner', '0018_auto_20211026_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='type_ticket',
            field=models.TextField(null=True),
        ),
    ]
