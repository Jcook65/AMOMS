from django.views import generic


class IndexView(generic.ListView):
    template_name = 'appointments/index.html'

    def get_queryset(self):
        return None