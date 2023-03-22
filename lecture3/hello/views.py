from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def mike(request):
    return HttpResponse("Hello, Mike!")


def jimmy(request):
    return HttpResponse("Hello, Jimmy!")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })


def index(request):
    return render(request, "hello/index.html")
