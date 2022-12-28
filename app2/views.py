from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def raja(request):
    return HttpResponse('<h2><marquee><i>he is good farmer in whole world</i></marquee></h2>')
def prakash(request):
    return HttpResponse('<b>he is unique boy in gurijala</b>')