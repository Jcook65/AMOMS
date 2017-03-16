from django.views import generic
from appointments.models import Appointment

class IndexView(generic.ListView):
    template_name = 'schedules/index.html'
    context_object_name = 'appointment_list'
    
    def get_queryset(self):
        return Appointment.objects.all()
