
from django.urls import path
from .views import detail_page, homepage

urlpatterns = [
    path("<str:filter>/", homepage, name='azubi_list'),
    path('<str:filter>/<int:id>/', detail_page, name="detail"),
    # path('frmtest/', form_name_view, name="form_name")
]
