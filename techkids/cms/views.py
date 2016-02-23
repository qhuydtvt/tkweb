from django.http import HttpResponse
from django.shortcuts import render
from platform import python_version
from django.template import loader, Context
from .models import Node


# Create your views here.

def index(request):
    template = loader.get_template('cms/index.html')
    return HttpResponse(template.render(request))

def node(request):
    template = loader.get_template('cms/node.html')
    node = None
    if len(Node.objects) > 0:
         node = Node.objects[0]
    return HttpResponse(template.render(Context({"node" : node.title})))
    #return HttpResponse(node.title)
