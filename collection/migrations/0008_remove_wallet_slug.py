# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20151104_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='slug',
        ),
    ]
