from django.views import generic


class IndexView(generic.ListView):
    template_name = 'schedules/details.html'

    def get_queryset(self):
        return None
