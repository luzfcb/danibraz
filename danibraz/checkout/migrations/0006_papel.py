# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-21 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20171120_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(choices=[('ABEV3', 'AMBEV S/A'), ('BBAS3', 'BRASIL'), ('BBDC3', 'BRADESCO 3'), ('BBDC4', 'BRADESCO 4'), ('BBSE3', 'BBSEGURIDADE'), ('BRAP4', 'BRADESPAR'), ('BRFS3', 'BRF SA'), ('BRKM5', 'BRASKEM'), ('BRML3', 'BR MALLS PAR'), ('BVMF3', 'BMFBOVESPA'), ('CCRO3', 'CCR SA'), ('CIEL3', 'CIELO'), ('CMIG4', 'CEMIG'), ('CSAN3', 'COSAN'), ('CSNA3', 'SID NACIONAL'), ('ECOR3', 'ECORODOVIAS'), ('ELET3', 'ELETROBRAS'), ('EMBR3', 'EMBRAER'), ('EQTL3', 'EQUATORIAL'), ('ESTC3', 'ESTACIO PART'), ('FIBR3', 'FIBRIA'), ('GGBR4', 'GERDAU'), ('GOAU4', 'GERDAU MET'), ('HYPE3', 'HYPERMARCAS'), ('ITSA4', 'ITAUSA'), ('ITUB4', 'ITAUUNIBANCO'), ('JBSS3', 'JBS'), ('KLBN11', 'KLABIN S/A'), ('KROT3', 'KROTON'), ('LAME4', 'LOJAS AMERIC'), ('LREN3', 'LOJAS RENNER'), ('MRVE3', 'MRV'), ('MULT3', 'MULTIPLAN'), ('NATU3', 'NATURA'), ('PCAR4', 'P.ACUCAR-CBD'), ('PETR3', 'PETROBRAS'), ('PETR4', 'PETROBRAS'), ('QUAL3', 'QUALICORP'), ('RADL3', 'RAIADROGASIL'), ('RAIL3', 'RUMO S.A.'), ('RENT3', 'LOCALIZA'), ('SANB11', 'SANTANDER BR'), ('SBSP3', 'SABESP'), ('SUZB5', 'SUZANO PAPEL'), ('TAEE11', 'TAESA'), ('UGPA3', 'ULTRAPAR'), ('USIM5', 'USIMINAS'), ('VALE3', 'VALE'), ('VIVT4', 'TELEF BRASIL'), ('WEGE3', 'WEG')], max_length=100, verbose_name='Papel')),
                ('stock', models.PositiveSmallIntegerField(verbose_name='Estoque')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Papeis',
            },
        ),
    ]
