from django.urls import path

from solomons_corner.views import index

urlpatterns = [
    path("", index, name="solomons_corner")
]