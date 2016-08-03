# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profils', '0007_profil_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(unique=True)),
                ('id_message', models.IntegerField(unique=True)),
                ('auteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profils.Profil')),
            ],
        ),
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='sujet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum.Sujet'),
        ),
    ]
