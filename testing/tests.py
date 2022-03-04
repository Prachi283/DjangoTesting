# Testing Models 

from django.test import TestCase
from testing.models import Employee

class EmployeeTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData: Run once to set up non-modified data for all class methods.
        Employee.objects.create(first_name="Prachi",last_name="PAtil")

    def test_first_name_label(self):
        emp=Employee.objects.get(id=1)
        field_label=emp._meta.get_field('first_name').verbose_name
        # self.assertTrue(field_label=='first_name')
        self.assertEqual(field_label,'first_name')

    def test_first_name_max_length(self):
        emp=Employee.objects.get(id=1)
        max_length=emp._meta.get_field('first_name').max_length
        self.assertEqual(max_length,200)