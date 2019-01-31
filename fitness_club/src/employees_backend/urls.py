from django.conf.urls import url
from . import views

module_name = 'employees_backend'

urlpatterns = [
    url(r'^employee_create/$',
            views.EmployeeCreateView.as_view(section=module_name),
            name='employee_create'),
    url(r'^employees_list/$',
            views.EmployeesListView.as_view(section=module_name),
            name='employees_list'),
    url(r'^employees_list_data/$', 
            views.EmployeesListData.as_view(),
            name='employees_list_data'),
    url(r'^employee_edit/$',
            views.EmployeeEditView.as_view(),
            name='employee_edit_blind'),
    url(r'^employee_edit/(?P<pk>\d+)/$',
            views.EmployeeEditView.as_view(section=module_name),
            name='employee_edit'),
    url(r'^employee_delete/$',
            views.EmployeeDeleteView.as_view(section=module_name),
            name='employee_delete_blind'),
    url(r'^employee_delete/(?P<pk>\d+)/$',
            views.EmployeeDeleteView.as_view(section=module_name),
            name='employee_delete_blind'),
]