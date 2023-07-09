from django.contrib import admin

from .models import Employee, Department, EmployeeDepartment

#class APIAdmin(admin.ModelAdmin):
#    list_display = 

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(EmployeeDepartment)
