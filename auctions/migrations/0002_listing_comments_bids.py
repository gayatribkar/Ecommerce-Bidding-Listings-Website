# Generated by Django 4.0.3 on 2022-09-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=128)),
                ('price', models.IntegerField()),
                ('image_url', models.URLField(blank=True)),
                ('category', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('commenter', models.ManyToManyField(blank=True, to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bids', models.IntegerField()),
                ('bidders', models.ManyToManyField(blank=True, to='auctions.listing')),
            ],
        ),
    ]
