from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('sign-up/', RegisterForm.as_view(), name = 'register'),
    path('login/', LoginForm.as_view(), name = 'login'),
]