# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0019_auto_20170715_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bulletin',
            old_name='img_photo',
            new_name='photo280_400',
        ),
        migrations.AddField(
            model_name='bulletin',
            name='photo280_400_2',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='photo450_300',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
    ]
