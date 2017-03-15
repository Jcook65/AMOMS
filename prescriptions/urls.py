from django.conf.urls import url
from . import views

app_name = 'prescriptions'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]