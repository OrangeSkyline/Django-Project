from django.http import HttpResponse
from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def index(request):
    # Retrieve the active portfolios from the database
    active_portfolios = Portfolio.objects.filter(
    is_active=True
    )
    
    return render(
        request,
        "portfolio_app/index.html",
        {"active_portfolios": active_portfolios}
    )
