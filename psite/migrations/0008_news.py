# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-17 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psite', '0007_track_apple_music_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
