# Generated by Django 2.2.1 on 2019-09-24 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0003_loginuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_label', models.CharField(max_length=32)),
                ('type_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Saller.LoginUser'),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.ImageField(default='img/02.jpg', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_count',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_location',
            field=models.CharField(max_length=254, verbose_name='产地'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_name',
            field=models.CharField(max_length=32, verbose_name='商品名字'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_number',
            field=models.CharField(max_length=11, verbose_name='商品编号'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_price',
            field=models.FloatField(verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_safe_date',
            field=models.IntegerField(verbose_name='保质期'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Saller.GoodsType'),
        ),
    ]