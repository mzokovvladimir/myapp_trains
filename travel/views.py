from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Vladimir'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'About us'
    return render(request, 'about.html', {'name': name})
