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

def courses(request):
    template = loader.get_template('cms/courses.html')
    return HttpResponse(template.render(request))

def contact(request):
    template = loader.get_template('cms/contact.html')
    return HttpResponse(template.render(request))


def course_single(request, course_id):
    template = loader.get_template('cms/course_single.html')
    return HttpResponse(template.render(request))
