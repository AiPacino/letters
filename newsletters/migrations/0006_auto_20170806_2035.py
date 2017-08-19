# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0005_auto_20170806_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('newsletter', 'url')]),
        ),
    ]