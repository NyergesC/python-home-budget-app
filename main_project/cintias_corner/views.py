from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse(
        "<h1>Welcome to Cintias Corner!</h1> <br>"
        "Happy Coding!!"
    )