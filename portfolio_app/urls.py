from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("portfolios/", views.portfolio, name="portfolio_list"),
    path("portfolios/<int:pk>/", views.PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("admin/", views.index, name="admin"),
    
]