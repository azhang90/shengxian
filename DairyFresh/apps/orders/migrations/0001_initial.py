# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('price', models.DecimalField(verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7', max_digits=10, decimal_places=2)),
                ('comment', models.TextField(default=b'', verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe4\xbf\xa1\xe6\x81\xaf')),
            ],
            options={
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=64, serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7', primary_key=True)),
                ('total_count', models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x80\xbb\xe6\x95\xb0')),
                ('total_amount', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x80\xbb\xe9\x87\x91\xe9\xa2\x9d', max_digits=10, decimal_places=2)),
                ('trans_cost', models.DecimalField(verbose_name=b'\xe8\xbf\x90\xe8\xb4\xb9', max_digits=10, decimal_places=2)),
                ('pay_method', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f', choices=[(1, b'\xe8\xb4\xa7\xe5\x88\xb0\xe4\xbb\x98\xe6\xac\xbe'), (2, b'\xe6\x94\xaf\xe4\xbb\x98\xe5\xae\x9d')])),
                ('status', models.SmallIntegerField(default=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), (2, b'\xe5\xbe\x85\xe5\x8f\x91\xe8\xb4\xa7'), (3, b'\xe5\xbe\x85\xe6\x94\xb6\xe8\xb4\xa7'), (4, b'\xe5\xbe\x85\xe8\xaf\x84\xe4\xbb\xb7'), (5, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('trade_id', models.CharField(max_length=100, unique=True, null=True, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
            ],
            options={
                'db_table': 'df_order_info',
            },
        ),
    ]
