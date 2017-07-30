# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0002_auto_20170708_1719'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bullentin',
            new_name='Bulletin',
        ),
    ]
