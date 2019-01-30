from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from django.views.generic import CreateView, TemplateView, View, UpdateView, DeleteView
from account.models import User, EmployeeProfile
from .forms import EmployeeForm
from django.core.urlresolvers import reverse_lazy
from fitness_club_app.extras import AjaxRequired
from preserialize.serialize import serialize
from django.http import JsonResponse

class EmployeesListView(Section, EmployeeLoginRequired, TemplateView):
    template_name = 'employees_backend/employees_list.html'

class EmployeeCreateView(Section, EmployeeLoginRequired, CreateView):
    template_name = 'employees_backend/employee_create_and_update.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees_backend:employees_list')

class EmployeesListData(EmployeeLoginRequired, AjaxRequired, View):

    def get_users_serialize_template(self):
        users_template = { 
            'fields': ['id', 'first_name', 'last_name', 'email'],
        }
        return users_template

    def get(self, request):
        users = User.objects.filter(is_employee=True)
        users_serialized = serialize(users, **self.get_users_serialize_template())
        return JsonResponse({'data': users_serialized}, safe=False)

class EmployeeEditView(Section, EmployeeLoginRequired, UpdateView):
    template_name = 'employees_backend/employee_create_and_update.html'
    model = User
    form_class = EmployeeForm
    success_url = reverse_lazy('employees_backend:employees_list')

    def get_form_kwargs(self):
        kwargs = super(EmployeeEditView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
        })
        return kwargs
    
class EmployeeDeleteView(Section, EmployeeLoginRequired, DeleteView):
    template_name = 'employees_backend/employee_delete.html'
    model = User
    success_url = reverse_lazy('employees_backend:employees_list')