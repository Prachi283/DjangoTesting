from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Employee
from rest_framework import generics 
from .serializers import EmployeeSerializer

class EmployeeListView(ListView):
	model=Employee
	paginate_by=10

class EmployeeView(DetailView):
	model=Employee

class CreateEmployeeApiView(generics.CreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer