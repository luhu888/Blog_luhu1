# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-26 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('url', models.CharField(max_length=200, verbose_name='指向地址')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='排序(越大的越靠后)')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '导航条',
                'verbose_name': '导航条',
                'ordering': ['order'],
            },
        ),
    ]