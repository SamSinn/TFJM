# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_auto_20160724_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='side_image',
            field=models.ImageField(default=1, upload_to='photos/'),
            preserve_default=False,
        ),
    ]