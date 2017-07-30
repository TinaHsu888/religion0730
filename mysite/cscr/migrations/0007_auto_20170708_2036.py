# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0006_auto_20170708_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
