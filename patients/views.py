from django.views import generic
from .models import Patient


class IndexView(generic.ListView):
    template_name = 'patients/patients.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        return Patient.objects.all()


class DetailView(generic.DetailView):
    model = Patient
    template_name = 'patient/detail.html'
