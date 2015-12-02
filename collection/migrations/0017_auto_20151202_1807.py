# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_auto_20151127_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='files',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=b'johndoe@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(default=b'john', max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(default=b'doe', max_length=50),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(default=1, to='collection.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(default=100, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=b'john', to=settings.AUTH_USER_MODEL),
        ),
    ]
