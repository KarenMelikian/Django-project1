from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (UserLoginView,
                    UserRegistrationView,
                    UserProfileView,
                    user_logout,
                    user_cart
                    )

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('user-cart/', user_cart, name='user-cart'),
    path('logout/', user_logout, name='logout')
]