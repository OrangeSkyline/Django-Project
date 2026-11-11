from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio_list"),
    path("home/", views.portfolio, name="portfolio_list"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path("portfolios/<int:pk>/", views.PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("admin/", views.index, name="admin"),
    
]