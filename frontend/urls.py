from django.urls import path
from .views import ManagerLoginView, LoggedInView, logout_view, EmployeesView, DepartmentsView, EmployeeEditView, DepartmentEditView, AssignmentEditView, AssignmentsView, PromotableEmployeesView, PromotionView

app_name = 'frontend'

urlpatterns = [
    path('login/', ManagerLoginView.as_view(), name='manager_login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', LoggedInView.as_view(), name='employees'),
    path('', LoggedInView.as_view(), name='employees'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees/add/', EmployeeEditView.as_view(), name='employee_add'),
    path('employees/edit/<int:pk>/', EmployeeEditView.as_view(), name='employee_edit'),
    path('departments/', DepartmentsView.as_view(), name='departments'),
    path('departments/add/', DepartmentEditView.as_view(), name='department_add'),
    path('departments/edit/<int:pk>/', DepartmentEditView.as_view(), name='department_edit'),
    path('assignments/', AssignmentsView.as_view(), name='assignments'),
    path('assignments/add/', AssignmentEditView.as_view(), name='assignment_add'),
    path('assignments/edit/<int:pk>/', AssignmentEditView.as_view(), name='assignment_edit'),
    path('employees/promotable/', PromotableEmployeesView.as_view(), name='promotable_employees'),
    path('employees/promote/<int:pk>/', PromotionView.as_view(), name='promote_employee'),
   
    
]

