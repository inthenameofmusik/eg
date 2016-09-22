# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200)),
                ('personal_url', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soundcloud_url', models.CharField(max_length=500)),
                ('spotify_url', models.CharField(max_length=500)),
                ('youtube_url', models.CharField(max_length=500)),
                ('apple_music_url', models.CharField(max_length=500)),
                ('tidal_url', models.CharField(max_length=500)),
                ('collaborators', models.ManyToManyField(to='psite.Collaborator')),
            ],
        ),
    ]
