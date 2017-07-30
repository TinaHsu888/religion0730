# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0009_database_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='schoar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('publications_list', models.CharField(max_length=500, blank=True)),
                ('publications_url', models.CharField(max_length=500, blank=True)),
                ('mail', models.CharField(max_length=300)),
            ],
        ),
    ]
