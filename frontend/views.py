from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from employees.models import Employee, Department, EmployeeDepartment
from .forms import EmployeeForm, DepartmentForm, AssignmentForm
from django.views import View
from django.views.generic import ListView
from datetime import date


class PromotionView(View):
    template_name = 'promote_employee.html'

    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, self.template_name, {'employee': employee})

    def post(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.promotion_date = date.today()
        employee.save()
        return redirect('frontend:promotable_employees')

class PromotableEmployeesView(View):
    template_name = 'promotable_employees.html'

    def get(self, request):
        today = date.today()
        promotable_employees = Employee.objects.filter(
                date_of_joining__lte=today.replace(year=today.year - 5),
                promotion_date__isnull=True 
                )
        return render(request, self.template_name, {'promotable_employees': promotable_employees})



class AssignmentsView(ListView):
    template_name = 'assignments.html'
    model = EmployeeDepartment
    context_object_name = 'assignments'


class AssignmentEditView(View):
    template_name = 'assignment_edit.html'

    def get(self, request, pk=None):
        if pk:
            assignment = EmployeeDepartment.objects.get(pk=pk)
            form = AssignmentForm(instance=assignment)
        else:
            form = AssignmentForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=None):
        if pk:
            assignment = EmployeeDepartment.objects.get(pk=pk)
            form = AssignmentForm(request.POST, instance=assignment)
        else:
            form = AssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('frontend:assignments')

        return render(request, self.template_name, {'form': form})


class ManagerLoginView(LoginView):
    template_name = 'manager_login.html'


class LoggedInView(LoginRequiredMixin, TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve all employees and departments from the database
        employees = Employee.objects.all()
        departments = Department.objects.all()

        context['employees'] = employees
        context['departments'] = departments

        return context


class EmployeesView(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context

class DepartmentsView(TemplateView):
    template_name = 'departments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

class EmployeeEditView(View):
    template_name = 'employee_edit.html'

    def get(self, request, pk=None):
        if pk:
            employee = Employee.objects.get(pk=pk)
            form = EmployeeForm(instance=employee)
        else:
            form = EmployeeForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=None):
        if pk:
            employee = Employee.objects.get(pk=pk)
            form = EmployeeForm(request.POST, instance=employee)
        else:
            form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('frontend:employees')

        return render(request, self.template_name, {'form': form})

class DepartmentEditView(View):
    template_name = 'department_edit.html'

    def get(self, request, pk=None):
        if pk:
            department = Department.objects.get(pk=pk)
            form = DepartmentForm(instance=department)
        else:
            form = DepartmentForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, pk=None):
        if pk:
            department = Department.objects.get(pk=pk)
            form = DepartmentForm(request.POST, instance=department)
        else:
            form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('frontend:departments')

        error = "Invalid form data."
        return render(request, self.template_name, {'form': form, 'error': error })


def logout_view(request):
    logout(request)
    return redirect('frontend:manager_login')



