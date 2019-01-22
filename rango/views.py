from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse(reverse('about'))
