from __future__ import unicode_literals

from django.db import models
from login import models as employeeModels


class Prescription(models.Model):
    prescriptionID = models.PositiveIntegerField(primary_key=True)
    prescriptionTxt = models.TextField()
    printTime = models.DateTimeField()
    employeeID = models.ForeignKey(employeeModels.Employee)
    createdTime = models.DateTimeField()
    prescriptionTitle = models.CharField(max_length=250)
