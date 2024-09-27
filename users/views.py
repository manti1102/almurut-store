from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.
class UserRegistrationView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class UserMakeLogoutView(View):
    """Вью, чтобы выйти из аккаунта"""

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login.html')

class UserMakeLoginView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data['email_address']
        password = data['password']


        user = CustomUser.objects.get(email=email)
        print('пользователь ', user)

        correct = user.check_password(password)
        print('коррект равен ', correct)

        if correct == True:
            login(request, user)
            return render(request,'login.html', context={'logged_in': True})
        else:
            return render(request, 'login.html', context={'logged_in': False})





class UserMakeRegistrationView(View):

    def post(self, request, *args, **kwargs):
        data =request.POST


        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email_address']
            user = CustomUser.objects.create_user(
                password=password1, first_name=first_name,
                email=email, last_name=last_name,
            )
            return render(request, 'product-list.html')
        else:
            pass