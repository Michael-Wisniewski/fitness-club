from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, HTML, Button, Div
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'publish', 'status', 'image')

    def __init__(self, **kwargs):
        super(PostForm, self).__init__(**kwargs)
        cancel_url = kwargs['initial']['cancel_url']
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Field('title'),
            Field('slug'),
            Field('author'),
            Field('body'),
            Div(
                'publish',
                css_id = 'datetimepicker'
            ),
            Field('status'),
            Field('image'),
            ButtonHolder(
                Submit('submit', 'Submit'),
                HTML("<a class='btn btn-secondary' href='{}'>Cancel</a>".format(cancel_url)),
            )
        )