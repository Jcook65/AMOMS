from __future__ import unicode_literals

from django.db import models
from login import models as employeeModels


class Schedule(models.Model):
    scheduleID = models.PositiveIntegerField(primary_key=True, max_length=255)
    dayOfWeek = models.DateField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    employeeID = models.ForeignKey(employeeModels.Employee)

