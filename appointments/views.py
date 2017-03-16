from django.views import generic


class IndexView(generic.ListView):
    template_name = 'appointments/details.html'

    def get_queryset(self):
        return None