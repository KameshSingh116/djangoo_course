from django.shortcuts import render

#First we will dive into function based views and later we we will go for the class based views.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Radhe radhe i am a hacked</h1>")

def success_page(request):
    return HttpResponse("<h1>This is a sign that you have succesfully retrieved your system</h1>")
