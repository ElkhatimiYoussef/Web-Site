from django import views
from django.urls import path
from . import views #Pour importer view

urlpatterns = [
  path('', views.home, name='home'), #it's how we create a view call home
]
