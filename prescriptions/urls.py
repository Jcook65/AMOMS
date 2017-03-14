from django.conf.urls import url
from . import views

app_name = 'prescriptions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]