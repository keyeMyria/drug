# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-07 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0022_auto_20181206_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen', models.CharField(max_length=10, verbose_name='\u7b5b\u9009\u7c7b\u522b')),
                ('work_name', models.CharField(max_length=100, verbose_name='work_name')),
                ('affinity', models.FloatField(verbose_name='affinity')),
                ('path', models.FileField(upload_to=b'', verbose_name='out_file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
            },
        ),
    ]
