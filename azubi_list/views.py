from django.shortcuts import render
from django.http import HttpResponse
from azubi_list.models import azubi_tbl, kaufmann

# Create your views here.

def azubi_list(request):
    return render(request, "azubi_list.html")

def index(request):
    azub_list = azubi_tbl.objects.order_by("Id")
    table_dict = {'azubi_table': azub_list}

    return render(request, 'index.html', context= table_dict)

def help(request):
    helpDict = {'help_insert': "HELP PAGE"}
    return render(request, 'help.html', context= helpDict)
