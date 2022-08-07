from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'pages/home.html')#function qui retourn tous qui est a home pages


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
