from django.db import models

# Create your models here.
class Employee(models.Model):
    
   
    employee_name =  models.CharField(max_length=200,blank=True)
    employee_email =  models.CharField(max_length=200,blank=True)
    employee_address  = models.CharField(max_length=200,blank=True)

    
   