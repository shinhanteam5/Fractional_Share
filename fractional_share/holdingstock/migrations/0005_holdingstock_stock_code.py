# Generated by Django 4.1.7 on 2023-02-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holdingstock', '0004_alter_holdingstock_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='holdingstock',
            name='stock_code',
            field=models.CharField(default=1, max_length=128, verbose_name='stock_name'),
            preserve_default=False,
        ),
    ]
