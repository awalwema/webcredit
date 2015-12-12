# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0021_auto_20151212_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
