# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0005_auto_20160724_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='sscategorie',
            name='image',
            field=models.ImageField(default=1, upload_to='photos/'),
            preserve_default=False,
        ),
    ]