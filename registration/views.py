from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'
