from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'login/index.html'

    def get_queryset(self):
        return None


class DashboardView(generic.ListView):
    template_name = 'login/home.html'

    def get_queryset(self):
        return None

class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login:home')

        return render(request, self.template_name, {'form':form})
