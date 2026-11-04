from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio, Student


# Create your views here.
def index(request):
    # Retrieve the index page
    return render(
        request,
        "portfolio_app/index.html"
    )

def portfolio(request):
    # Retrieve the active portfolios from the database
    active_portfolios = Portfolio.objects.filter(
    is_active=True
    )
    
    return render(
        request,
        "portfolio_app/portfolio_list.html",
        {"active_portfolios": active_portfolios}
    )

# CBV for All Students
class StudentListView(ListView):
    model = Student
    template_name = "portfolio_app/student_list.html"
    context_object_name = "students"
    
# CBV for One Student
class StudentDetailView(DetailView):
    model = Student
    template_name = "portfolio_app/student_detail.html"
    context_object_name = "student"
    
# CBV for One Portfolio
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_app/portfolio_detail.html"
    context_object_name = "portfolio"