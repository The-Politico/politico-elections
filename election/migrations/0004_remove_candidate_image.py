# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_auto_20171031_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='image',
        ),
    ]
