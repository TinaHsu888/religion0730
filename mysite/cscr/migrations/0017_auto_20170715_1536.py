# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0016_people_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='job_type',
        ),
        migrations.AddField(
            model_name='people',
            name='name_url',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
