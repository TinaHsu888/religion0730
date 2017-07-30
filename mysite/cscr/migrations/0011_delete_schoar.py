# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0010_people_schoar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='schoar',
        ),
    ]
