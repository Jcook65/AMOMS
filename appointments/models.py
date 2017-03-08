from __future__ import unicode_literals
from django.db import models
from patients import models as patientModels
from login import models as employeeModels

class Appointment(models.Model):
    appointmentID = models.PositiveIntegerField(primary_key=True)
    patientID = models.ForeignKey(patientModels.Patient)
    employeeID = models.ForeignKey(employeeModels.Employee)
    scheduledDate = models.DateField()
    scheduledTime = models.DateTimeField()
    notes = models.TextField()
    checkinTime = models.DateTimeField()
    checkoutTime = models.DateTimeField()
    appointmentStart = models.DateTimeField()
    appointmentEnd = models.DateTimeField()
