from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Div

class EmployeeLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(EmployeeLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('username', placeholder="Enter username or email"),
            Field('password', placeholder="Password"),
            Div(           
                Submit('submit', 'Log In', css_class="form-control"),
                css_class='button'
            ) 
        )

