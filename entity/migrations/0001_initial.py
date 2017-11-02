# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Bodies',
            },
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geography.Division')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='entity.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='entity.Body')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='geography.Division')),
                ('jurisdiction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='entity.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='body',
            name='jurisdiction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='body',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='entity.Body'),
        ),
    ]
