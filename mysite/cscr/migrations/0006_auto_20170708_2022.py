# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0005_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='img_url',
            field=models.CharField(max_length=225, blank=True),
        ),
    ]
