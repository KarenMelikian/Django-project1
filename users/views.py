from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, FormView

from .forms import UserLoginForm

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')


def registration(request):
    context = {
        'title': 'RegalRidge - Registration'
    }

    return render(request, 'users/registration.html', context)

# class RegistrationView(CreateView):
#     template_name = 'users/registration.html'
#
#     def get_queryset(self):
#         pass


class ProfileView(ListView):
    template_name = 'users/profile.html'

    def get_queryset(self):
        pass