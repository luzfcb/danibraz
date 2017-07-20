# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20170720_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.AddField(
            model_name='address',
            name='kynd',
            field=models.CharField(choices=[('P', 'PRINCIPAL'), ('C', 'COBRANÇA'), ('E', 'ENTREGA')], default=1, max_length=1, verbose_name='Tipo'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]