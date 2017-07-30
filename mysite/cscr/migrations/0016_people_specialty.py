# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0015_auto_20170708_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='specialty',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
