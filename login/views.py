from django.shortcuts import render
from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name = 'account/login.html'
