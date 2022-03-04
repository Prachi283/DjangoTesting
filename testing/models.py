from django.db import models

class Employee(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	emp_id=models.CharField(max_length=200)
	joining_date=models.DateField(null=True,blank=True)

	def get_absolute_url(self):
		return reverse('emp-detail',args=[str(self.id)])

	def __str__(self):
		return f"Name:{self.first_name} {self.last_name}"
		
