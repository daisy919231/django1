from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample_app(request):
    return HttpResponse('<h1>HI PYTHON!<h1>')