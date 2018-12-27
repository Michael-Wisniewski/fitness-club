from django.views.generic import FormView
from django_hosts.resolvers import reverse
from .forms import EmployeeLoginForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

class EmployeeLoginView(FormView):
    template_name = 'account/employee_login.html'
    form_class = EmployeeLoginForm
    response_message = ''

    def post(self, request):
        form = EmployeeLoginForm(self.request.POST)
        succesLoginFlag = False

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if not user.is_active:
                    self.response_message = 'Your account is not active.'
                elif not user.is_employee:
                    self.response_message = 'You don\'t have permission to acces this site'
                else:
                    succesLoginFlag = True     
            else:
                self.response_message = 'Wrong username or password'

        if succesLoginFlag:
            login(self.request, user)
            return HttpResponseRedirect(reverse('landing_page_backend', host='backend'))
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeLoginView, self).get_context_data(**kwargs)
        context['response_message'] = self.response_message
        return context

def EmployeeLogut(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_backend', host='backend'))