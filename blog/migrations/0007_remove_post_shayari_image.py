# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-04-14 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190414_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='shayari_image',
        ),
    ]
