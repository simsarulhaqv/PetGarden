# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantDetailPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CTIMES', models.CharField(max_length=30)),
                ('TEMP', models.IntegerField()),
                ('HUMID', models.IntegerField()),
                ('MOIST', models.IntegerField()),
                ('LIGHT', models.IntegerField()),
                ('SURFTEMP', models.IntegerField()),
                ('LEAFMOIST', models.IntegerField()),
                ('RTIME', models.IntegerField()),
            ],
        ),
    ]
