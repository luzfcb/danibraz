# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-20 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20171120_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([]),
        ),
    ]
