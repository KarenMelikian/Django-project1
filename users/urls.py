from django.urls import path

from .views import (LoginView,
                    registration,
                    ProfileView)

app_name = 'users'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('registration', registration, name='registration'),
    path('profile', ProfileView.as_view(), name='profile'),
]