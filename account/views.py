from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from vehicle.utils import assign_permissions

from django.views import View

class Home(View):
    def get(self, request):
        return render(request, 'account/home.html')
    

class RegisterForm(View):
    def get(self, request):
        form = Registration()
        return render(request, 'account/registration_form.html', {'form':form})
    
    def post(self, request):
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            assign_permissions(user, user.role)
            messages.success( request, 'Registration Successful!' )
            return redirect('login')
        return render(request, 'account/registration_form.html', {'form':form})


class LoginForm(View):
    def get(self, request):
        form = Login()
        return render(request, 'account/login_form.html', {'form': form})
    
    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            usrName = form.cleaned_data.get('user_name')
            pswrd = form.cleaned_data.get('password')
            # if usrName and pswrd:
            user = authenticate(user_name = usrName, password = pswrd)
            if user:
                login(request, user)
                return redirect('vehicle_detail')
            form.add_error(None, 'Invalide User name or password')
        return render(request, 'account/login_form.html', {'form': form})

