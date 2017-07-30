# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0008_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('url', models.CharField(max_length=300)),
                ('img_url', models.CharField(max_length=225, blank=True)),
                ('img_photo', models.ImageField(upload_to=b'static/cscr/img/', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('book_type', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=225, blank=True)),
                ('img_photo', models.ImageField(upload_to=b'static/cscr/img/', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
