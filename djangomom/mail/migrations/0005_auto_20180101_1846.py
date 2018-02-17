# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-01 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180101_1846'),
        ('mail', '0004_mail_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='users',
            field=models.ManyToManyField(related_name='users', to='account.UserAccount'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sent',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sent On'),
        ),
    ]
