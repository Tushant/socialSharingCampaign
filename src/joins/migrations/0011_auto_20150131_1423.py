# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0010_join_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='count',
        ),
        migrations.AddField(
            model_name='join',
            name='count_added',
            field=models.ForeignKey(related_name='count', blank=True, to='joins.Join', null=True),
            preserve_default=True,
        ),
    ]
