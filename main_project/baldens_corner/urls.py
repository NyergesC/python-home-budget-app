from django.urls import path

from baldens_corner.views import index

urlpatterns = [
    path("", index, name="baldens_corner")
]