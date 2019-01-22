from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>about </a>")

def about(request):
    return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index </a>")
