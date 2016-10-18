# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-17 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psite', '0009_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditableText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(editable=False, max_length=40, unique=True)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]