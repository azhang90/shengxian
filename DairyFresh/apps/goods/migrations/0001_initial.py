# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', tinymce.models.HTMLField(default=b'', verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbb\x8b\xe7\xbb\x8d', blank=True)),
            ],
            options={
                'db_table': 'df_goods',
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('logo', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86')),
                ('image', models.ImageField(upload_to=b'category', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'db_table': 'df_goods_category',
                'verbose_name': '\u5546\u54c1\u7c7b\u522b',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'db_table': 'df_goods_image',
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('unit', models.CharField(max_length=10, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe5\x8d\x95\xe4\xbd\x8d')),
                ('price', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=10, decimal_places=2)),
                ('stock', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('default_image', models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('status', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe7\xba\xbf')),
                ('category', models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='goods.GoodsCategory')),
                ('goods', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='goods.Goods')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name': '\u5546\u54c1SKU',
                'verbose_name_plural': '\u5546\u54c1SKU',
            },
        ),
        migrations.CreateModel(
            name='IndexCategoryGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('display_type', models.SmallIntegerField(verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe6\xa0\x87\xe9\xa2\x98'), (1, b'\xe5\x9b\xbe\xe7\x89\x87')])),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe9\xa1\xba\xe5\xba\x8f')),
                ('category', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x88\xab', to='goods.GoodsCategory')),
                ('sku', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_category_goods',
                'verbose_name': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
                'verbose_name_plural': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=b'banner', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe9\xa1\xba\xe5\xba\x8f')),
                ('sku', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_goods',
                'verbose_name': '\u4e3b\u9875\u8f6e\u64ad\u5546\u54c1',
                'verbose_name_plural': '\u4e3b\u9875\u8f6e\u64ad\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.URLField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe8\xbf\x9e\xe6\x8e\xa5')),
                ('image', models.ImageField(upload_to=b'banner', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe9\xa1\xba\xe5\xba\x8f')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
                'verbose_name_plural': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
            },
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU', to='goods.GoodsSKU'),
        ),
    ]
