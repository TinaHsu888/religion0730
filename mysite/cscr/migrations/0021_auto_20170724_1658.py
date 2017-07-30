# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0020_auto_20170724_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('published_date', models.CharField(max_length=20, blank=True)),
                ('book_type', models.CharField(max_length=500, blank=True)),
                ('author', models.CharField(max_length=100, blank=True)),
                ('img_url', models.CharField(max_length=225, blank=True)),
                ('img_photo', models.ImageField(upload_to=b'static/cscr/img/', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='published_date',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='book_type',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
