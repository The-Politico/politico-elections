# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theshow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personimage',
            name='tag',
            field=models.SlugField(help_text='Used to serialize images. <b>Must be unique per person.</b>'),
        ),
    ]
