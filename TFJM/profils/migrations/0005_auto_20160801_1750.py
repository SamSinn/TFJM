# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0004_auto_20160801_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id_user',
            field=models.IntegerField(unique=True),
        ),
    ]
