from django.http import HttpResponse
from django.template import loader
from prescriptions.models import Diagnoses
import json 

def index(request):
    
    template = loader.get_template('patients/patients.html')
    patientName = "Adam Coker"
    sex = "M"
    Weight = "140"
    Age = "100"
    Height = "6\'1\""
    diag = Diagnoses()
    diag.diagnosesID = 1
    diag.diagnosesDateBegin = "12/0/0"
    diag.diagnosesDateEND = "12/1/0"
    diag.diagnosesName = "test"
    diag.diagnosesSeverity = "low"
    diags = [diag]
    diags = serializers.serialize
    context = {
        "patientName": patientName, "sex" : sex, "weight": Weight, "age":Age, "height": Height,
        
    }
    return HttpResponse(template.render(context, request))