# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-04-14 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='post',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
