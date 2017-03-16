from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


class Employee(User):
    employeeID = models.PositiveIntegerField(primary_key=True)
    # username = models.CharField(max_length=50, null=False)
    # password = models.CharField(max_length=128, null=False)
    access = (
        ("R", "Receptionist"),
        ("P", "Practitioner"),
        ("A", "Admin"),
    )
    access = models.CharField(max_length=1, choices=access, default="R", null=False)

    def get_absolute_url(self):
        return reverse('patients:home', kwargs={'pk':self.pk})
