
from django.urls import path
from .views import detail_page, homepage

urlpatterns = [
    path("", homepage, name='azubi_list'),
    path('<int:id>/', detail_page, name="detail")
]
