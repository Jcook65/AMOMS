from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Patient
from .forms import DiagForm, NotesForm, PrescriptionForm

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

class DiagnosisView(View):
    form_class = DiagForm
    template_name = 'patients/diagnosis.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

class PrescriptionView(View):
    form_class = PrescriptionForm
    template_name = 'patients/prescription.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

class NotesView(View):
    form_class = NotesForm
    template_name = 'patients/notes.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})