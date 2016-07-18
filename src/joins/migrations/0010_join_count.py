# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0009_auto_20150131_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='count',
            field=models.IntegerField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
