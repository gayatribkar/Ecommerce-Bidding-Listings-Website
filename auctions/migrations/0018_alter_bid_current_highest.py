# Generated by Django 4.0.3 on 2022-09-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_bid_current_highest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='current_highest',
            field=models.BooleanField(null=True),
        ),
    ]
