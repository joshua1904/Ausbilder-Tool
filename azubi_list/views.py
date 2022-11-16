from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Azubi, Profession
from django.shortcuts import get_object_or_404, render
from .forms import SearchForm
import operator




# def form_name_view(request):
#     form = FormName()
#     return render(request, "azubi_detail.html", {"formi":form})

class failureObject():
    first_name = "Keine Treffer"
    id = 0
def detail_page(request, filter, id):
    form = SearchForm()
    obj = get_object_or_404(Azubi, pk=id)
    azubis = Azubi.objects.order_by('-last_name', "first_name")
    azubis = sort(azubis)
    professions = Profession.objects.all()
    departments = Azubi.objects.values_list('department')
    final_list = get_filter(filter, azubis)
    return render(request, "azubi_detail.html", {"obj": obj, "azubis": final_list, "professions": professions, "departments": departments, "filter": filter, "form": form})   

#Ruft die selbe seite wie Detail page auf, braucht aber keine obj id (Vlt geht das ja aber auch besser)
def homepage(request, filter: str):
    azubis = Azubi.objects.order_by("last_name")
    azubis = sort(azubis)
    form = SearchForm()
    professions = Profession.objects.all()
    departments = Azubi.department
    final_list = get_filter(filter, azubis)
    if request.method == "POST":
        search = request.POST['azubi_search_input']
        final_list = get_search(final_list, search)   
    if len(final_list) > 0:
        return render(request, "azubi_detail.html", {"azubis": final_list, "obj": final_list[0], "professions": professions, "departments": departments, "filter": filter, "form": form})
    return render(request, "azubi_detail.html", {"azubis": azubis,"professions": professions, "departments": departments, "filter": filter, "form": form})

def get_search(azubis: Azubi, search_str: str):
    final_list = list(filter(lambda x: f"{x.first_name}{x.last_name}".__contains__(search_str), azubis))
    if len(final_list) == 0:
        print(final_list)
        #faked Daten eines Azubis zur Fehleranzeige
        final_list = [failureObject()]
    return final_list

def get_filter(filter_: str, azubis):
    temp_list = list()
    #if filter_ == "profession":
    final_list = list(filter(lambda x: x.topic.name == filter_, azubis))
    if filter_ == "department":
        final_list = list(filter(lambda x: x.department.name == filter_, azubis))
    if filter_ == "all":
        final_list = azubis
    #mydata = Azubi.objects.filter_(topic=filter_).values()
    #mydata = Azubi.objects.filter_(topic=filter_, id=2).values()
    #final_list = list(mydata)
    return final_list

def sort(azubis) -> list:  
    sorted_list =  sorted(azubis, key=operator.attrgetter('email'))
    return sorted_list

def customize(request):
    azubis = Azubi.objects.all()
    return render(request, "customize.html", {"azubis", azubis})
