# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20151030_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='docfile',
            field=models.FileField(upload_to=b'files/%Y/%m/%d'),
        ),
    ]
