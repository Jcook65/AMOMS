from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Patient, Notes
from prescriptions.models import Diagnoses, Prescription
from .forms import DiagForm, NotesForm, PrescriptionForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'patients/patients.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        return Patient.objects.all()


class DetailView(generic.DetailView):
    model = Patient
    template_name = 'patients/details.html'
    slug_field = 'patientID'
    pk_url_kwarg = 'patientID'


class DiagnosisView(CreateView):
    model = Diagnoses
    fields = ['diagnosesName', 'diagnosesDateBegin', 'diagnosesSeverity', ]



class PrescriptionView(CreateView):
    model = Prescription
    fields = ['prescriptionTitle', 'prescriptionTxt', 'createdTime', ]


class NotesView(CreateView):
    model = Notes
    fields = ['noteText', ]
