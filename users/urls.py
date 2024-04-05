from django.urls import path
from .views import (LoginView,
                    RegistrationView,
                    ProfileView,
                    logout_user)

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout')
]