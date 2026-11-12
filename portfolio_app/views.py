from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio, Project, Student
from django.urls import reverse_lazy


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
   
# CBV for One Project    
class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio_app/project_detail.html"
    context_object_name = "project"

# CBV for Creating a Student
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','major']
    template_name = "portfolio_app/student_form_create.html"
    success_url = reverse_lazy('student_list')

# CBV for Updating a Student
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','major']
    template_name = "portfolio_app/student_form_update.html"

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.pk})

# CBV for Deleting a Student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "portfolio_app/student_form_delete.html"
    success_url = reverse_lazy('student_list')
    
# CBV for Creating a Portfolio
class PortfolioCreateView(CreateView):
    model = Portfolio
    fields = ['student','title','about','is_active']
    template_name = "portfolio_app/portfolio_form_create.html"
    success_url = reverse_lazy('portfolio_list')

# CBV for Updating a Portfolio
class PortfolioUpdateView(UpdateView):
    model = Portfolio
    fields = ['student','title','contact_email','about','is_active']
    template_name = "portfolio_app/portfolio_form_update.html"

    def get_success_url(self):
        return reverse_lazy('portfolio_detail', kwargs={'pk': self.object.pk})

# CBV for Deleting a Portfolio
class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = "portfolio_app/portfolio_form_delete.html"
    success_url = reverse_lazy('portfolio_list')