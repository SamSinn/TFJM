# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0007_profil_bio'),
        ('forum', '0002_remove_sujet_createur'),
    ]

    operations = [
        migrations.AddField(
            model_name='sujet',
            name='createur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profils.Profil'),
            preserve_default=False,
        ),
    ]