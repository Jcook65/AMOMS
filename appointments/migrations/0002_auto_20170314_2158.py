# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentID',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]