from django.shortcuts import render
from .models import Azubi, Profession
from django.shortcuts import get_object_or_404, render
# Create your views here.

def detail_page(request, id, filter):
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.all()
    final_list = get_filter(filter, azubis)
    return render(request, "azubi_detail.html", {"obj": obj, "azubis": final_list, "filter": filter})   

#Ruft die selbe seite wie Detail page auf, braucht aber keine obj id (Vlt geht das ja aber auch besser)
def homepage(request, filter: str):
    azubis = Azubi.objects.all()
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    if len(final_list) > 0:
        return render(request, "azubi_detail.html", {"azubis": final_list, "obj": final_list[0], "professions": professions, "filter": filter})
    return render(request, "azubi_detail.html", {"azubis": azubis, "filter": filter})

def get_filter(filter: str, azubis):
    final_list = list()
    for azubi in azubis:
        if azubi.topic.name == filter:
            final_list.append(azubi)
    if filter == "all":
        final_list = azubis
    return final_list
