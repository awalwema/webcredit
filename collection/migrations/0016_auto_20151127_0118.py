# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0015_auto_20151126_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', models.DecimalField(max_digits=7, decimal_places=2)),
                ('files', models.ForeignKey(to='collection.File')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='balance',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to='collection.UserProfile'),
        ),
    ]
