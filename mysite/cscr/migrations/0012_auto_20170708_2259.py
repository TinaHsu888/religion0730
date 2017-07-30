# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0011_delete_schoar'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='job_title',
            field=models.CharField(default=b'pp', max_length=1, choices=[(b'pp', b'people'), (b'com', b'committee'), (b'sch', b'scholar'), (b'adm', b'administrative')]),
        ),
        migrations.AddField(
            model_name='people',
            name='mail',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='publications_list',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='publications_url',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
