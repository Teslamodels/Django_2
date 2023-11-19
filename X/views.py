from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def HomePageView(request):
    return HttpResponse('Welcome to my site')

class Temp(TemplateView):
    template_name = 'index.html'