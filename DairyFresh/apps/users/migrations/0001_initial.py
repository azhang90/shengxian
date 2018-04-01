# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}, max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', verbose_name='groups', related_name='user_set', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', verbose_name='user permissions', related_name='user_set', blank=True, to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'db_table': 'df_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('receiver', models.CharField(max_length=10)),
                ('addr', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=6)),
                ('phone_numer', models.CharField(max_length=11)),
                ('isDefault', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'df_address',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(null=True, to='users.AreaInfo', blank=True)),
            ],
            options={
                'db_table': 'df_area',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(related_name='city', to='users.AreaInfo'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(related_name='district', to='users.AreaInfo'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(related_name='province', to='users.AreaInfo'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
