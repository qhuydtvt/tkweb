from django.http import HttpResponse
from django.shortcuts import render
from platform import python_version
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('cms/index.html')
    return HttpResponse(template.render(request))

def about(request):
    template = loader.get_template('cms/about_us.html')
    return HttpResponse(template.render(request))