# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-29 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0010_auto_20180529_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
