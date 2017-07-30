# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0017_auto_20170715_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='People_Administrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('name_url', models.CharField(max_length=500, blank=True)),
                ('specialty', models.CharField(max_length=100, blank=True)),
                ('text', models.TextField(blank=True)),
                ('publications_list', models.CharField(max_length=500, blank=True)),
                ('publications_url', models.CharField(max_length=500, blank=True)),
                ('mail', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People_Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('name_url', models.CharField(max_length=500, blank=True)),
                ('specialty', models.CharField(max_length=100, blank=True)),
                ('text', models.TextField(blank=True)),
                ('publications_list', models.CharField(max_length=500, blank=True)),
                ('publications_url', models.CharField(max_length=500, blank=True)),
                ('mail', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People_Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('name_url', models.CharField(max_length=500, blank=True)),
                ('specialty', models.CharField(max_length=100, blank=True)),
                ('text', models.TextField(blank=True)),
                ('publications_list', models.CharField(max_length=500, blank=True)),
                ('publications_url', models.CharField(max_length=500, blank=True)),
                ('mail', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People_scholar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('name_url', models.CharField(max_length=500, blank=True)),
                ('specialty', models.CharField(max_length=100, blank=True)),
                ('text', models.TextField(blank=True)),
                ('publications_list', models.CharField(max_length=500, blank=True)),
                ('publications_url', models.CharField(max_length=500, blank=True)),
                ('mail', models.CharField(max_length=300, blank=True)),
            ],
        ),
    ]
