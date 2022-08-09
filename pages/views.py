from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)#function qui retourn tous qui est a home pages


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)#We Past The Data


def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
