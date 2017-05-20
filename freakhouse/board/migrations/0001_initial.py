# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 14:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import freakhouse.board.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Original name')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('hash', models.CharField(blank=True, max_length=32, verbose_name='Hash')),
                ('file', models.FileField(upload_to=freakhouse.board.models.files_resolver, verbose_name='Location')),
                ('thumb', models.ImageField(upload_to=freakhouse.board.models.thumbs_resolver, verbose_name='Thumbnail')),
                ('image_width', models.PositiveSmallIntegerField(blank=True, verbose_name='Image width')),
                ('image_height', models.PositiveSmallIntegerField(blank=True, verbose_name='Image height')),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension', models.CharField(max_length=10, verbose_name='Extension')),
                ('mime', models.CharField(max_length=250, verbose_name='MIME')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.PositiveIntegerField(blank=True, db_index=True, verbose_name='PID')),
                ('op_post', models.BooleanField(default=False, verbose_name='First post in thread')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Bump')),
                ('poster', models.CharField(blank=True, max_length=32, null=True, verbose_name='Name')),
                ('tripcode', models.CharField(blank=True, max_length=32, verbose_name='Tripcode')),
                ('email', models.CharField(blank=True, max_length=32, verbose_name='Email')),
                ('topic', models.CharField(blank=True, max_length=48, verbose_name='Topic')),
                ('password', models.CharField(blank=True, max_length=64, verbose_name='Password')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('message_html', models.TextField(blank=True)),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.File')),
            ],
            options={
                'ordering': ['pid'],
                'get_latest_by': 'pid',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=5, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('force_files', models.BooleanField(default=True, verbose_name='Force to post file on thread creation')),
                ('filesize_limit', models.PositiveIntegerField(default=10485760, verbose_name='Filesize limit')),
                ('anonymity', models.BooleanField(default=False, verbose_name='Force anonymity')),
                ('default_name', models.CharField(default='Anonymous', max_length=64, verbose_name='Default poster name')),
                ('bumplimit', models.PositiveSmallIntegerField(default=500, verbose_name='Max posts in thread')),
                ('threadlimit', models.PositiveSmallIntegerField(default=200, verbose_name='Max threads')),
                ('threads_per_page', models.PositiveSmallIntegerField(default=20, verbose_name='Max threads on page')),
                ('file_types', models.ManyToManyField(to='board.FileType')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bump', models.DateTimeField(blank=True, db_index=True, verbose_name='Bump')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Section')),
            ],
            options={
                'ordering': ['-bump'],
                'get_latest_by': 'bump',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Thread'),
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.FileType'),
        ),
    ]