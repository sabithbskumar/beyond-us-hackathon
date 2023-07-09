from django import forms
from employees.models import Employee, Department, EmployeeDepartment

class EmployeeForm(forms.ModelForm):
    date_of_joining = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    promotion_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDepartment
        fields = '__all__'
