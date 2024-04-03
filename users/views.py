from django.shortcuts import render
from django.views.generic import View, CreateView, ListView


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')



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