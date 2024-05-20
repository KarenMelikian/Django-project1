from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from cart.models import Cart
from order.models import Order, OrderItem


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


@method_decorator(login_required, name='dispatch')
class UserProfileView(FormView, LoginRequiredMixin):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = '/user/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        ).order_by("-id")
        return context


def user_cart(request):
    return render(request, 'users/user-cart.html')

def user_logout(request):
    logout(request)
    messages.success(request, f'{request.user.username} You are logged out of your account.')
    return redirect(reverse('main:index'))