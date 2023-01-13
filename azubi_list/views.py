from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Azubi, Profession
from django.shortcuts import get_object_or_404, render
from .forms import SearchForm, AzubiForm, ProfessionForm, DeleteForm
import operator
from .scripts import change_training_year_if_neccessary
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

#wird genutzt falls keine Azubis in der Liste sind
class failureObject():
    first_name = "Keine Treffer"
    id = 0


def homepage(request, filter: str, year: int, id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    change_training_year_if_neccessary()
    azubis = Azubi.objects.order_by("last_name")
    form = SearchForm()
    professions = Profession.objects.all()
    final_list = get_filter(filter, azubis)
    final_list = get_year_filter(year, final_list)
    if request.method == "POST":
        try:
            search = request.POST['azubi_search_input']
            final_list = get_search(final_list, search)
        except:
            pass
  
    if len(final_list) > 0:
        if id == 0:
            return render(request, "azubi_detail_2.html", {"azubis": final_list, "obj": final_list[0], "professions": professions, "filter": filter, "form": form, "year": year, "id":id})
        obj = get_object_or_404(Azubi, pk=id)
        return render(request, "azubi_detail_2.html", {"azubis": final_list, "obj": obj, "professions": professions, "filter": filter, "form": form, "year": year, "id":id})
    return render(request, "azubi_detail_2.html", {"azubis": final_list,"professions": professions, "filter": filter, "form": form, "year": year, "id": id})

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


def get_year_filter(year_filter: int, azubis: list):
    final_list = list()
    final_list = list(filter(lambda x: x.year == year_filter, azubis))
    if year_filter == 0:
        final_list = azubis
    return final_list

def sort(azubis) -> list:  
    sorted_list =  sorted(azubis, key=operator.attrgetter('email'))
    return sorted_list

def start_page(request):
    return homepage(request, "all", 0, 0)


def add_azubi(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    azubi_form = AzubiForm()
    profession_form = ProfessionForm()
    context = {"azubi_form": azubi_form, "profession_form": profession_form  }
    if request.method == "POST":
        azubi_form = AzubiForm(request.POST)
        if azubi_form.is_valid():
            azubi_form.save()
        else:
            print("Fehler beim Azubi Hinzufügen")
    return render(request, "add_azubi.html", context)

def delete_confirm(request, id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    filter = "all"
    azubi = get_object_or_404(Azubi, pk=id)
    context = {"azubi": azubi, "filter": filter}

    if request.method == "POST":
        print("hi_2")
        azubi.delete()
        return homepage(request, "all", 0, 0)
    return render(request, "delete_confirm.html", context)

def delete_azubi(request, id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    azubi = get_object_or_404(Azubi, pk=id)
    
    if request.method == 'POST':
        azubi.delete()

    return homepage(request, "all", 0, 0)


def edit_azubi_data(request, id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    azubi = get_object_or_404(Azubi, pk=id)
    if request.method == 'POST':
        form = AzubiForm(request.POST, instance=azubi)
        if form.is_valid():
            form.save()
            return homepage(request, "all", 0, id)
    else:
        form = AzubiForm(instance=azubi)

    context = {"azubi": azubi, "form": form}
    return render(request, 'change_azubi_values.html', context)


def settings(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    context = {}
    return render(request, 'settings.html', context)

def add_proffesion(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    profession_form = ProfessionForm()
    context= {"profession_form": profession_form}
    if request.method == "POST":
        profession_form = ProfessionForm(request.POST)
        if profession_form.is_valid():
            profession_form.save()
        else:
            print("Fehler beim Beruf Hinzufügen")
    return render(request, "add_profession.html", context)

def login_required(request):
    return render(request, "login_required.html", {})



def logout_view(request):
    logout(request)
    return login_required(request)
    