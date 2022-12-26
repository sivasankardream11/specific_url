from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def raja(request):
    return HttpResponse('<h2> This is app2 raja view</h2>')
def rani(request):
    return HttpResponse('<h2> This is app2 rani view</h2>')