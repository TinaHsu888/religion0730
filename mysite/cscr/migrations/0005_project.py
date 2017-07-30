# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0004_bulletin_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.CharField(max_length=300, blank=True)),
            ],
        ),
    ]
