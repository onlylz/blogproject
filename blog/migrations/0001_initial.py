# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tele',
            fields=[
                ('ag_port', models.TextField(db_column='AG_port')),
                ('number', models.TextField(primary_key=True, serialize=False)),
                ('depart', models.TextField(blank=True, null=True)),
                ('person', models.TextField(blank=True, null=True)),
                ('floor', models.TextField(blank=True, null=True)),
                ('number_110_frame', models.TextField(blank=True, db_column='110_frame', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tele',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeleOld20170407',
            fields=[
                ('ag_port', models.TextField(db_column='AG_port')),
                ('number', models.TextField(primary_key=True, serialize=False)),
                ('depart', models.TextField(blank=True, null=True)),
                ('floor', models.TextField(blank=True, null=True)),
                ('number_110_frame', models.TextField(blank=True, db_column='110_frame', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': '_tele_old_20170407',
                'managed': False,
            },
        ),
    ]
