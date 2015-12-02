# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0017_auto_20151202_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('user', models.ForeignKey(to='collection.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
