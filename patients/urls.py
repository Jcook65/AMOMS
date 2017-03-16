from django.conf.urls import url
from . import views

app_name = 'patients'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<patientID>[0-9]+)$', views.DetailView.as_view(), name='details'),
]