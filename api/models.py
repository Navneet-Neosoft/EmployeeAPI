from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    designation = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name
