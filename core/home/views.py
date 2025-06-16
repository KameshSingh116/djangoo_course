from django.shortcuts import render

#First we will dive into function based views and later we we will go for the class based views.

from django.http import HttpResponse

def home(request):
    peoples= [
        {"name":"Krishn", "Age":27},
        { "name":"Radha", "Age":28},
         {"name":"Balram", "Age":29}
         
    ]

    vegies=["Brinjal", "Potato", "Beetroot", "Cucumber"]

    text="""Radhe Radhe Hare Krishna"""

    return render(request, 'index.html', context = {"peoples":peoples,"text":text,"vegies":vegies})

def success_page(request):
    return HttpResponse("<h1>This is a sign that you have succesfully retrieved your system</h1>")

def about(request):
    context={'page':'About'}
    return render(request, 'about.html',context)

def contact(request):
    context ={'page':'Contact'}
    return render(request, 'contact.html',context)