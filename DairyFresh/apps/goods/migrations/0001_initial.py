# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='名称', max_length=100)),
                ('desc', tinymce.models.HTMLField(default='', verbose_name='详细介绍', blank=True)),
            ],
            options={
                'db_table': 'df_goods',
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='名称', max_length=20)),
                ('logo', models.CharField(verbose_name='标识', max_length=100)),
                ('image', models.ImageField(upload_to='category', verbose_name='图片')),
            ],
            options={
                'db_table': 'df_goods_category',
                'verbose_name_plural': '商品类别',
                'verbose_name': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='goods', verbose_name='图片')),
            ],
            options={
                'db_table': 'df_goods_image',
                'verbose_name_plural': '商品图片',
                'verbose_name': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='名称', max_length=100)),
                ('title', models.CharField(verbose_name='简介', max_length=200)),
                ('unit', models.CharField(verbose_name='销售单位', max_length=10)),
                ('price', models.DecimalField(max_digits=10, verbose_name='价格', decimal_places=2)),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('default_image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.BooleanField(default=True, verbose_name='是否上线')),
                ('category', models.ForeignKey(verbose_name='类别', to='goods.GoodsCategory')),
                ('goods', models.ForeignKey(verbose_name='商品', to='goods.Goods')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name_plural': '商品SKU',
                'verbose_name': '商品SKU',
            },
        ),
        migrations.CreateModel(
            name='IndexCategoryGoodsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('display_type', models.SmallIntegerField(choices=[(0, '标题'), (1, '图片')], verbose_name='展示类型')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('category', models.ForeignKey(verbose_name='商品类别', to='goods.GoodsCategory')),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_category_goods',
                'verbose_name_plural': '主页分类展示商品',
                'verbose_name': '主页分类展示商品',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_goods',
                'verbose_name_plural': '主页轮播商品',
                'verbose_name': '主页轮播商品',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='活动名称', max_length=50)),
                ('url', models.URLField(verbose_name='活动连接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name_plural': '主页促销活动',
                'verbose_name': '主页促销活动',
            },
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU'),
        ),
    ]
