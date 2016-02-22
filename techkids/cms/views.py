from django.http import HttpResponse
from django.shortcuts import render
from platform import python_version

# Create your views here.

def index(request):
    return HttpResponse("Hello, this is TechKids CMS, running on Python " + python_version())