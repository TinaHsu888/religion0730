# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0022_auto_20170726_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'verbose_name': '\u6700\u65b0\u6d88\u606f', 'verbose_name_plural': '\u6700\u65b0\u6d88\u606f'},
        ),
        migrations.AddField(
            model_name='bulletin',
            name='top',
            field=models.CharField(default=b'g', max_length=1, verbose_name='\u7f6e\u9802', choices=[(b't', '\u7f6e\u9802'), (b'g', '\u4e00\u822c')]),
        ),
    ]
