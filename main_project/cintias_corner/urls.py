from django.urls import path

from cintias_corner.views import index

urlpatterns = [
    path("", index, name="cintias_corner")
]