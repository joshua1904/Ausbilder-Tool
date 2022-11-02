
from django.urls import path, include
from .views import Azubi_List

urlpatterns = [
    path("", Azubi_List.as_view(), name='azubi_list')
]
