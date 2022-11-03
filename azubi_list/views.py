from django.shortcuts import render
from .models import Azubi
from django.shortcuts import get_object_or_404, render
# Create your views here.

def detail_page(request, id):
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.all()
    return render(request, "azubi_detail.html", {"obj": obj, "azubis": azubis})   

#Ruft die selbe seite wie Detail page auf, braucht aber keine obj id (Vlt geht das ja aber auch besser)
def homepage(request):
    azubis = Azubi.objects.all()
    if len(azubis) > 0:
        return render(request, "azubi_detail.html", {"azubis": azubis, "obj": azubis[0]})
    return render(request, "azubi_detail.html", {"azubis": azubis})
