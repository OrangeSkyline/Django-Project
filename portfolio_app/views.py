from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
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
        "portfolio_app/portfolios.html",
        {"active_portfolios": active_portfolios}
    )

# CBV for Students
class StudentListView(ListView):
    model = Student
    template_name = "portfolio_app/student_list.html"
    context_object_name = "students"
