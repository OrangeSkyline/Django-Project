from django.db import models

# Student Class.
class Student(models.Model):
    MAJOR = (
        ("CSCI-BS", "BS in Computer Science"),
        ("CPEN-BS", "BS in Computer Engineering"),
        ("BIGD-BI", "BI in Game Design and Development"),
        ("BICS-BI", "BI in Computer Science"),
        ("BISC-BI", "BI in Computer Security"),
        ("CSCI-BA", "BA in Computer Science"),
        ("DASE-BS", "BS in Data Analytics and Systems Engineering"),
    )

    name = models.CharField("First & Last Name", max_length=60)
    email = models.EmailField("MSU Email")
    major = models.CharField(max_length=60, choices=MAJOR, blank=True)

    def __str__(self):
        return f"{self.name}"

# Portfolio Class.
class Portfolio(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.student.name}'s Portfolio: {self.title}"

# Project Class.
class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.portfolio.student.name}'s Project"
    