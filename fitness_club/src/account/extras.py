from django.shortcuts import HttpResponseRedirect
from django_hosts import reverse

class EmployeeLoginRequired():

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated() and\
           self.request.user.is_employee :
           return super(EmployeeLoginRequired, self).dispatch(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login_backend', host='backend'))   