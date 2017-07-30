# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0014_auto_20170708_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
