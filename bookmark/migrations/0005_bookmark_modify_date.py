# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-08 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_remove_bookmark_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modify_date'),
        ),
    ]