# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girasol', '0009_auto_20161125_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='links',
            field=models.ManyToManyField(related_name='_post_links_+', to='girasol.Post'),
        ),
    ]
