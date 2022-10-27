from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from azubi_list.models import AzubiData, My_List
# Create your views here.

def azubi_list(request):
    return render(request, "azubi_list/test.html", context={"insert": "Juhu"})


class list_of_Azubis(ListView):
    model = AzubiData


def detail_page(request, id):
    obj = get_object_or_404(AzubiData, pk=id)
    return render(request, "detail.html", {"obj": obj})

