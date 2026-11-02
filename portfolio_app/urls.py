from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("portfolios/", views.portfolio, name="portfolios"),
    path("admin/", views.index, name="admin"),
    
]