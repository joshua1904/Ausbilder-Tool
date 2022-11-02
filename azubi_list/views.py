from django.shortcuts import render
from django.views.generic import ListView
from .models import Azubi
# Create your views here.

class Azubi_List(ListView):
    model = Azubi
    template_name = "home.html"