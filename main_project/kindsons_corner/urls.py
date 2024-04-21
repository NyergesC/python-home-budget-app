from django.urls import path

from kindsons_corner.views import index

urlpatterns = [
    path("", index, name="kindsons_corner")
]