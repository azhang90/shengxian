# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='address',
            field=models.ForeignKey(verbose_name=b'\xe6\x94\xb6\xe8\x8e\xb7\xe5\x9c\xb0\xe5\x9d\x80', to='users.Address'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe4\xb8\x8b\xe5\x8d\x95\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95', to='orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x95\x86\xe5\x93\x81', to='goods.GoodsSKU'),
        ),
    ]
