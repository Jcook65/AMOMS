from django.contrib import admin
from .models import Prescription, Diagnoses
# Register your models here.

admin.site.register(Prescription)
admin.site.register(Diagnoses)
