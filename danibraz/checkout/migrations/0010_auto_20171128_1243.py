# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-28 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20171128_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(verbose_name='quantity'),
        ),
    ]
