# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-29 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0008_auto_20180529_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcart',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ykea.Client'),
        ),
        migrations.AlterField(
            model_name='clientcart',
            name='shoppingcart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ykea.Shoppingcart'),
        ),
    ]
