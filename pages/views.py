from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

def hello(request):
    return HttpResponse('hello world')

class AboutPageView(TemplateView):
    template_name = 'about.html'

# Create your views here.
