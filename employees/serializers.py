from rest_framework import serializers
from .models import Employee, Department, EmployeeDepartment

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'
        
    def get_department(self, obj):
        try:
            department = EmployeeDepartment.objects.get(employee=obj).department
            return {
                'department_id': department.id,
                'department_name': department.name,
                'department_location': department.location,
                'department_manager_id': department.manager_id,
            }
        except EmployeeDepartment.DoesNotExist:
            return None
    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

