# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 18:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160808_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
