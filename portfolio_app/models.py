from django.db import models

# Student Class
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

    name = models.CharField(max_length=30)
    email = models.EmailField("Enter your MSU Email here.")
    major = models.CharField(max_length=40, choices=MAJOR, blank=True)

    def __str__(self):
        return self.name
