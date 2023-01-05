from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.core import serializers
from .models import Members
from .models import Capacity
import json

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def member(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('member.html')
    context = {'mymembers': mymembers,}
    return HttpResponse(template.render(context, request))

def capacity(request):
    mycapacity = Capacity.objects.all()
    template = loader.get_template('capasity.html')
    data  = serializers.serialize('json', mycapacity)
    context = {'mycapacity': data,}
    return HttpResponse(template.render(context, request))

def select(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
