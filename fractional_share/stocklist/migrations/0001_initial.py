# Generated by Django 4.1.7 on 2023-02-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=16, verbose_name='stock_name')),
                ('current_price', models.IntegerField(verbose_name='current_price')),
                ('high_rate', models.IntegerField(max_length=64, verbose_name='high_rate')),
                ('trading_volume', models.IntegerField(max_length=32, verbose_name='trading_volume')),
                ('category', models.CharField(max_length=16, verbose_name='category')),
            ],
            options={
                'verbose_name': '주식리스트',
                'verbose_name_plural': '주식리스트',
                'db_table': 'stock_list',
            },
        ),
    ]
