# This file allows you to control what the viewer sees when they visit the application.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Think of each view as something the user wants to see.

def index(request):
    return HttpResponse("Hello!")