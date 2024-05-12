from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render (request, 'solomons_corner/profile.html')