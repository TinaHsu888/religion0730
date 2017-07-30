# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cscr', '0018_people_administrator_people_committee_people_researcher_people_scholar'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='people_administrator',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='people_committee',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='people_researcher',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
        migrations.AddField(
            model_name='people_scholar',
            name='img_photo',
            field=models.ImageField(upload_to=b'static/cscr/img/', blank=True),
        ),
    ]
