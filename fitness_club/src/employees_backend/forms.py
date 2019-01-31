from django import forms
from betterforms.multiform import MultiModelForm
from account.models import User, EmployeeProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, **kwargs):
        super(UserForm, self).__init__(**kwargs)
        if 'instance' in kwargs:
            self.fields.pop('password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ('picture', 'miniature', 'description')

class EmployeeForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': UserProfileForm,
    }

    def __init__(self, **kwargs):
        super(EmployeeForm, self).__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        objects = super(EmployeeForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.is_employee = True
            if 'password' in self.cleaned_data['user']:
                user.set_password(user.password)
            user.save()
            profile = objects['profile']
            profile.user = user
            profile.save()

        return objects