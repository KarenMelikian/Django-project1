from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (login,
                    registration,
                    UserProfileView,
                    user_logout,
                    user_cart
                    )

app_name = 'users'


urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('user-cart/', user_cart, name='user-cart'),
    path('logout/', user_logout, name='logout')
]