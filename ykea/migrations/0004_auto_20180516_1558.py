# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-16 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0003_auto_20180506_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='featured_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='instructions',
            field=models.FileField(upload_to=''),
        ),
    ]
