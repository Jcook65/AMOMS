from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^/register/$', views.UserFormView.as_view(), name='register'),

    url(r'^/dashboard/$', views.DashboardView.as_view(), name='home'),


]
