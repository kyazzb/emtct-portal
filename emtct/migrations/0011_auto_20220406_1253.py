# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2022-04-06 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emtct', '0010_rapidpro_smschannel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rapidpro',
            old_name='smsChannel',
            new_name='sms_channel',
        ),
    ]