from django.urls import path

from azubi_list.views import list_of_Azubis, detail_page



urlpatterns = [
    path("test/", list_of_Azubis.as_view(), name="test"),
    path("<int:id>", detail_page, name="detail")
]
