from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    context = {}
    return render(request, 'login/index.html', context)

def home(request):
    context = {}
    return render(request, 'login/index.html', context)

