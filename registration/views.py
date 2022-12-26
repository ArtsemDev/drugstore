from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('signin')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('index')
