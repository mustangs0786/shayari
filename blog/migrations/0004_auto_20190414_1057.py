# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-04-14 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190414_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='shayari_image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
