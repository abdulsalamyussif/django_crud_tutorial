from django.shortcuts import render
from .models import Employee
# Create your views here.
 
def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees':employees})