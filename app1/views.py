from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mouni(request):
    return HttpResponse('<marquee>mounika reddy</marquee>')

def chandu(request):
    return HttpResponse('<b><marquee><h1>chandana reddy</h1></marquee></h1></b>')