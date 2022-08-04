from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'pages/home.html')#function qui retourn tous qui est a home pages

