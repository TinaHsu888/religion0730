# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0007_auto_20170708_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('img_url', models.CharField(max_length=225, blank=True)),
                ('img_photo', models.ImageField(upload_to=b'static/cscr/img/', blank=True)),
                ('video_url', models.CharField(max_length=500, blank=True)),
            ],
        ),
    ]
