# Generated by Django 2.2.1 on 2019-10-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0010_delete_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_address', models.TextField()),
                ('user_code', models.CharField(max_length=32)),
                ('user_phone', models.CharField(max_length=11)),
                ('status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saller.LoginUser')),
            ],
        ),
    ]
