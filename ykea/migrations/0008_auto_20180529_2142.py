# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-29 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0007_auto_20180529_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcart',
            name='shoppingcart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ykea.Shoppingcart'),
        ),
    ]