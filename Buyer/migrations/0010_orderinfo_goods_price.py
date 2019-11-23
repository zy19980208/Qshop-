# Generated by Django 2.2.1 on 2019-09-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0009_remove_orderinfo_goods_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='goods_price',
            field=models.FloatField(default=10, verbose_name='商品单价'),
            preserve_default=False,
        ),
    ]
