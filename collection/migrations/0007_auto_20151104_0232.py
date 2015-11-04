# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='wallet',
            new_name='balance',
        ),
        migrations.AddField(
            model_name='wallet',
            name='slug',
            field=models.SlugField(default=99, unique=True),
            preserve_default=False,
        ),
    ]
