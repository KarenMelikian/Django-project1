from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, ListView, FormView, TemplateView, DetailView

from .forms import UserLoginForm, UserRegistrationForm

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')


class RegistrationView(FormView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context



def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('main:index'))