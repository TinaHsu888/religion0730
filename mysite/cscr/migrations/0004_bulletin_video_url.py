# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0003_auto_20170708_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='video_url',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
