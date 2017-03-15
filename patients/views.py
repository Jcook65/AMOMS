from django.http import HttpResponse
from django.template import loader
from prescriptions.models import Diagnoses
from .models import Patient
import json 

def index(request):
    
    patient = Patient.objects.all()
    patient = patient[0]
    template = loader.get_template('patients/patients.html')
    
    
    context = {
        'patient' : patient,
        
    }
    return HttpResponse(template.render(context, request))