from django.contrib import admin
from .models import Patient, Notes
# Register your models here.

admin.site.register(Patient)
admin.site.register(Notes)
