from django.views import generic


class IndexView(generic.ListView):
    template_name = 'schedules/index.html'

    def get_queryset(self):
        return None
