from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(arg):
    return HttpResponse("Hello world")
