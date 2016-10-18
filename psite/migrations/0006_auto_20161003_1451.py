# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psite', '0005_track_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='track',
            name='spotify_html',
            field=models.CharField(default='<iframe src="https://embed.spotify.com/?uri=spotify%3Atrack%3A6pf6iatLx7YFxtmcQiUxJa" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>', max_length=600, verbose_name='Spotify HTML'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='track',
            name='apple_music_url',
            field=models.CharField(max_length=500, verbose_name='Apple Music URL'),
        ),
        migrations.AlterField(
            model_name='track',
            name='soundcloud_html',
            field=models.CharField(max_length=500, verbose_name='SoundCloud HTML'),
        ),
        migrations.AlterField(
            model_name='track',
            name='spotify_url',
            field=models.CharField(max_length=500, verbose_name='Spotify URL'),
        ),
        migrations.AlterField(
            model_name='track',
            name='tidal_url',
            field=models.CharField(max_length=500, verbose_name='Tidal URL'),
        ),
        migrations.AlterField(
            model_name='track',
            name='youtube_url',
            field=models.CharField(max_length=500, verbose_name='YouTube URL'),
        ),
    ]