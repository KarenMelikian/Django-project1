from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from cart.models import Cart

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username}, you are logged in to your account.')
        return super().form_valid(form)



class UserRegistrationView(FormView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username}, you are successfully registered.')
        return super().form_valid(form)



class UserProfileView(FormView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = '/user/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs


def user_cart(request):
    cart = Cart.objects.all()
    return render(request, 'users/user-cart.html', {'carts': cart})

def user_logout(request):
    logout(request)
    messages.success(request, f'{request.user.username} you are logged out of your account.')
    return redirect(reverse('main:index'))