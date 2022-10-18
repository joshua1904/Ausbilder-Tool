from django.shortcuts import render

# Create your views here.

def azubi_list(request):
    return render(request, "azubi_list.html")
