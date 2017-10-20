# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0002_auto_20171017_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntersectRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intersection', models.DecimalField(blank=True, decimal_places=6, help_text='The portion of the to_division that intersects this division.', max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='peerrelationship',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='peerrelationship',
            name='from_division',
        ),
        migrations.RemoveField(
            model_name='peerrelationship',
            name='to_division',
        ),
        migrations.RemoveField(
            model_name='division',
            name='peers',
        ),
        migrations.DeleteModel(
            name='PeerRelationship',
        ),
        migrations.AddField(
            model_name='intersectrelationship',
            name='from_division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='geography.Division'),
        ),
        migrations.AddField(
            model_name='intersectrelationship',
            name='to_division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='geography.Division'),
        ),
        migrations.AddField(
            model_name='division',
            name='intersecting',
            field=models.ManyToManyField(help_text='Intersecting divisions intersect this one geographically but do not necessarily have a parent/child relationship. The relationship between a congressional district and a precinct is an example of an intersecting relationship.', related_name='_division_intersecting_+', through='geography.IntersectRelationship', to='geography.Division'),
        ),
        migrations.AlterUniqueTogether(
            name='intersectrelationship',
            unique_together=set([('from_division', 'to_division')]),
        ),
    ]