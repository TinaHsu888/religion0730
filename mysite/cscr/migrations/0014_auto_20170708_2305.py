# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0013_auto_20170708_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='job_type',
            field=models.CharField(default=b'pp', max_length=3, choices=[(b'pp', b'people'), (b'com', b'committee'), (b'sch', b'scholar'), (b'adm', b'administrative')]),
        ),
        migrations.AlterField(
            model_name='people',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
    ]
