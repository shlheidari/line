from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def member(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('member.html')
    context = {'mymembers': mymembers,}
    return HttpResponse(template.render(context, request))

def capacity(request):
  template = loader.get_template('capasity.html')
  return HttpResponse(template.render())

def select(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
