from django.views import generic


class IndexView(generic.FormView):
    template_name = 'login/index.html'

class DashboardView(generic.FormView):
    template_name = 'login/home.html'
