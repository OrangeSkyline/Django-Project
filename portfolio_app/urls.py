from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio_list"),
    path("home/", views.portfolio, name="portfolio_list"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("portfolios/<int:pk>/", views.PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("admin/", views.index, name="admin"),
    
]