# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0020_auto_20151206_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.AlterField(
            model_name='file',
            name='docfile',
            field=models.FileField(upload_to=b'files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
