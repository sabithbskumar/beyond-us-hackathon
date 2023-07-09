from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee, Department, EmployeeDepartment
from .serializers import EmployeeSerializer, DepartmentSerializer
from datetime import date



class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeDepartmentAssignmentView(APIView):
    def post(self, request, employee_id, department_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            department = Department.objects.get(id=department_id)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'}, status=404)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found.'}, status=404)

        assignment, _ = EmployeeDepartment.objects.get_or_create(employee=employee)
        assignment.department = department
        assignment.save()

        return Response({'message': 'Employee successfully assigned to the department.'}, status=200)


class PromotionAPIView(APIView):
    def post(self, _, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if employee has more than 5 years of experience
        years_of_experience = (date.today() - employee.date_of_joining).days // 365
        if years_of_experience >= 5:
            # Perform promotion
            employee.promotion_date = date.today()
            employee.save()

            return Response({'message': 'Employee promoted successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Employee does not meet promotion criteria.'}, status=status.HTTP_400_BAD_REQUEST)
