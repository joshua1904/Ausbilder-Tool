
from django.urls import path
from .views import detail_page, homepage, start_page, add_azubi, delete_azubi, delete_confirm, edit_azubi_data
urlpatterns = [
    path("<str:filter>/", homepage, name='azubi_list'),
    path('<str:filter>/<int:id>/', detail_page, name="detail"),
    path('', start_page, name="start"),
    path('add/azubi', add_azubi, name="add"),
    path('delete/<int:id>/', delete_azubi, name='delete'),
    path('delete/confirm/<int:id>', delete_confirm, name="deleteconfirm"),
    path('change/<int:id>', edit_azubi_data, name="edit")
]
