# Generated by Django 2.2.1 on 2019-09-25 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0006_orderinfo_goods_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='goods_price',
        ),
    ]