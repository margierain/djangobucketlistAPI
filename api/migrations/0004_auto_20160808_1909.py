# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_bucketlistitem_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.BucketList'),
        ),
    ]
