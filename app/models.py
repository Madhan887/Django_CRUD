from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=25)
    Position=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    