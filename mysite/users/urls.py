from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (login,
                    registration,
                    UserProfileView,
                    user_logout,
                    user_cart,
                    UserPasswordChangeView,
                    UserPasswordResetView,
                    UserPasswordResetDoneView,
                    UserPasswordResetConfirmView
                    )

app_name = 'users'


urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('user-cart/', user_cart, name='user-cart'),
    path('logout/', user_logout, name='logout'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('reset-password/', UserPasswordResetView.as_view(), name='password_reset'),
    path('reset-password-done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]