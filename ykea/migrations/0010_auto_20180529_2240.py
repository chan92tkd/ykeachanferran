# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-29 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ykea', '0009_auto_20180529_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcart',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientcart',
            name='shoppingcart',
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='ClientCart',
        ),
    ]
