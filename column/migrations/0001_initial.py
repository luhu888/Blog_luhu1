# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-26 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='专栏名称')),
                ('summary', models.TextField(verbose_name='专栏摘要')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ManyToManyField(to='article.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name_plural': '专栏',
                'verbose_name': '专栏',
                'ordering': ['-create_time'],
            },
        ),
    ]
