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
    if course_id == '1':
        template = loader.get_template('cms/course_ios.html')
    elif course_id == '2':
        template = loader.get_template('cms/course_android.html')
    elif course_id == '3':
        template = loader.get_template('cms/course_c4e.html')
    else
        template = loader.get_template('cms/courses.html')
    return HttpResponse(template.render(request))

def instructor_single(request, instructor_id):
    template = loader.get_template('cms/instructor.html')
    return HttpResponse(template.render(request))
