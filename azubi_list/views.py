from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Azubi
from django.shortcuts import get_object_or_404, render
# Create your views here.

class Azubi_List(ListView):
    queryset = Azubi.objects.all()
    template_name = "home.html"


def detail_page(request, id):
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.all()
    return render(request, "azubi_detail.html", {"obj": obj, "azubis": azubis})   


# class Azubi_Detail(DetailView):
#     queryset = Azubi.objects.all()
#     template_name = "azubi_detail.html"