from django.db import models
from datetime import date


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.manager and not self.manager.promotion_date:
            raise ValueError("Department manager eligiblity not met.")

        super().save(*args, **kwargs)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    promotion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.promotion_date:
            years_of_experience = (date.today() - self.date_of_joining).days // 365
            if years_of_experience < 5:
                raise ValueError("Promotion date cannot be set for employees with less than 5 years of experience.")
        super().save(*args, **kwargs)


class EmployeeDepartment(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.name
