# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0012_auto_20170708_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='job_title',
            field=models.CharField(default=b'pp', max_length=3, choices=[(b'pp', b'people'), (b'com', b'committee'), (b'sch', b'scholar'), (b'adm', b'administrative')]),
        ),
    ]
