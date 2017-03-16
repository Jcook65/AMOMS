from django.views import generic


class IndexView(generic.ListView):
    template_name = 'prescriptions/details.html'

    def get_queryset(self):
        return None