from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Azubi, Profession
from django.shortcuts import get_object_or_404, render
from .forms import SearchForm, AzubiForm
import operator


class failureObject():
    first_name = "Keine Treffer"
    id = 0
def detail_page(request, filter, id):
    form = SearchForm()
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.order_by('-last_name', "first_name")
    azubis = sort(azubis)
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    if request.method == "POST":
        search = request.POST['azubi_search_input']
        final_list = get_search(final_list, search)   
    return render(request, "azubi_detail_2.html", {"obj": obj, "azubis": final_list, "professions": professions, "filter": filter, "form": form})   

#Ruft die selbe seite wie Detail page auf, braucht aber keine obj id (Vlt geht das ja aber auch besser)
def homepage(request, filter: str):
    azubis = Azubi.objects.order_by("last_name")
    azubis = sort(azubis)
    form = SearchForm()
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    if request.method == "POST":
        search = request.POST['azubi_search_input']
        final_list = get_search(final_list, search)   
    if len(final_list) > 0:
        return render(request, "azubi_detail_2.html", {"azubis": final_list, "obj": final_list[0], "professions": professions, "filter": filter, "form": form})
    return render(request, "azubi_detail_2.html", {"azubis": azubis,"professions": professions, "filter": filter, "form": form})

def get_search(azubis: Azubi, search_str: str):
    final_list = list(filter(lambda x: f"{x.first_name}{x.last_name}".lower().__contains__(search_str.lower()), azubis))
    if len(final_list) == 0:
        #faked Daten eines Azubis zur Fehleranzeige
        final_list = [failureObject()]
    return final_list

def get_filter(profession_filter: str, azubis):
    final_list = list()
    final_list = list(filter(lambda x: x.topic.name == profession_filter, azubis))
    if profession_filter == "all":
        final_list = azubis
    return final_list

def sort(azubis) -> list:  
    sorted_list =  sorted(azubis, key=operator.attrgetter('email'))
    return sorted_list

def start_page(request):
    return homepage(request, "all")


def add_azubi(request):
    azubi_form = AzubiForm()
    context = {"form": azubi_form }
    if request.method == "POST":
        azubi_form = AzubiForm(request.POST)
        if azubi_form.is_valid():
            azubi_form.save()
        else:
            print("mies")
    return render(request, "add_azubi.html", context)
