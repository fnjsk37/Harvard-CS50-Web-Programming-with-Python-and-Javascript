# A list of all the available URLs for this application
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]