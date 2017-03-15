from django.conf.urls import url
from . import views

app_name = 'schedules'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^home/$', views.index, name='home')
]