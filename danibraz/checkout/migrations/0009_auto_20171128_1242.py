# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-28 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20171128_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10, verbose_name='quantity'),
        ),
    ]
