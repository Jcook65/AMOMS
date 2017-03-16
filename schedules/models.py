from __future__ import unicode_literals

from django.db import models
from login.models import Employee


class Schedule(models.Model):
    scheduleID = models.PositiveIntegerField(primary_key=True)
    dayOfWeek = models.DateField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    employeeID = models.ForeignKey(Employee)

