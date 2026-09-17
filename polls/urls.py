from django.urls import path

from . import views

urlpatterns = [
    path("https://www.orangeskyline.com", views.index, name="index")
]