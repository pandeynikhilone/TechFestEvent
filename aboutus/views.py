from django.shortcuts import render
from django.views.generic import TemplateView
from django import views

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'
