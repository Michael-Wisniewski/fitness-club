from fitness_club_app.extras import Section
from django.views.generic import ListView
from account.models import User

class EmployeesListView(Section, ListView):
    template_name = 'employees/sites/employees_list.html'
    queryset = User.objects.filter(is_employee=True)
    context_object_name = 'employees'