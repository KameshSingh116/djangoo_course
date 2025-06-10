from django.shortcuts import render

#First we will dive into function based views and later we we will go for the class based views.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Radhe radhe i am a hacked")
