# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_auto_20170308_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescriptionID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('prescriptionTxt', models.TextField()),
                ('printTime', models.DateTimeField()),
                ('createdTime', models.DateTimeField()),
                ('prescriptionTitle', models.CharField(max_length=250)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Employee')),
            ],
        ),
    ]
