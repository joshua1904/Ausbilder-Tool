from django.urls import path

from azubi_list.views import AzubiDetail, list_of_Azubis, detail_page, frame, list_of_Azubis2



urlpatterns = [
    path('', list_of_Azubis.as_view(), name="test"),
    path('<int:pk>', AzubiDetail.as_view(), name="detail"),
    path("frame", frame),
]
