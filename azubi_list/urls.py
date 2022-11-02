
from django.urls import path, include
from .views import Azubi_List, detail_page

urlpatterns = [
    path("", Azubi_List.as_view(), name='azubi_list'),
    path('<int:id>', detail_page, name="detail"),
]
