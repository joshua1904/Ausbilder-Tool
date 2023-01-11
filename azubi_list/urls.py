
from django.urls import path
from .views import homepage, start_page, add_azubi, delete_azubi, delete_confirm, edit_azubi_data, settings, add_proffesion
urlpatterns = [
    path("<str:filter>/<int:year>/<int:id>/", homepage, name='azubi_list'),
    path('', start_page, name="start"),
    path('add/azubi', add_azubi, name="add"),
    path('delete/<int:id>/', delete_azubi, name='delete'),
    path('delete/confirm/<int:id>', delete_confirm, name="deleteconfirm"),
    path('change/<int:id>', edit_azubi_data, name="edit"),
    path('settings/', settings, name="settings"),
    path('add/profession/', add_proffesion, name="add_profession")
]
