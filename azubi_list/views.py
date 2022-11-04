from django.shortcuts import render
from .models import Azubi, Profession
from django.shortcuts import get_object_or_404, render
# Create your views here.

def detail_page(request, id, filter):
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.all()
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    return render(request, "azubi_detail.html", {"obj": obj, "azubis": final_list, "professions": professions, "filter": filter})   

#Ruft die selbe seite wie Detail page auf, braucht aber keine obj id (Vlt geht das ja aber auch besser)
def homepage(request, filter: str):
    azubis = Azubi.objects.all()
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    if len(final_list) > 0:
        return render(request, "azubi_detail.html", {"azubis": final_list, "obj": final_list[0], "professions": professions, "filter": filter})
    return render(request, "azubi_detail.html", {"azubis": azubis,"professions": professions, "filter": filter})

def get_filter(profession_filter: str, azubis):
    final_list = list()
    final_list = list(filter(lambda x: x.topic.name == profession_filter, azubis))
    if profession_filter == "all":
        final_list = azubis
    return final_list
