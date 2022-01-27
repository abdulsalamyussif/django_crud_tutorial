from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=10)

    class Meta:
        db_table = 'employee'
    
   

