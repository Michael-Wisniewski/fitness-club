from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class FooterForm(forms.Form):
    about_us = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(required=False)
    post_code = forms.CharField(required=False)
    street = forms.CharField(required=False)
    number = forms.CharField(required=False)
    phone = forms.RegexField(label='Phone<br/>(format: xxx-xxx-xxx)', 
                             required=False,
                             regex=r'^\d{3}[--]\d{3}[--]\d{3}$')
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super(FooterForm, self).__init__(*args, **kwargs)
        data_dict = {}
        data_file = open("/fitness_club/src/footer_backend/data.txt")

        for line in data_file:
            line_arr = line.split(" ", 1)
            if len(line_arr) > 1:
                field = line_arr[0]
                value = line_arr[1]
                if field == 'about_us':
                    value = "\n".join(value.split('<br/>'))

                self.initial[field] = value 

        data_file.close()
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Field('about_us'),
            Field('city'),
            Field('post_code'),
            Field('street'),
            Field('number'),
            Field('phone'),
            Field('email'),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

