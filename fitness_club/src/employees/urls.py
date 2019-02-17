from django.conf.urls import url
from . import views

module_name = 'employees'

urlpatterns = [
    url(r'^$', 
            views.EmployeesListView.as_view(section=module_name),
            name='employees_list'),
]