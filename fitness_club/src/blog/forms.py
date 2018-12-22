from django import forms
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML, Row, Div
from custom_crispy_forms.layout import PostTitleField 
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)
    title = forms.CharField()
    url = forms.URLField()

    def send_email(self):
        cd = self.cleaned_data
        subject = '{} ({}) invites you to read "{}"'.format(cd['name'], cd['email'], cd['title'])
        message = 'You can read post "{}", by clicking on the link below:\n\n{}\n\nComment added by {}.'\
                  .format(cd['title'], cd['url'], cd['name'], cd['comment'])        
        send_mail(subject, message, 'info@fitnessclub.pl', [cd['to']])
        pass   

    def __init__(self,**kwargs):
        super(EmailPostForm, self).__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            PostTitleField('title'),
            Field('name', placeholder="Your name"),
            Field('email', placeholder="Your email"),
            Field('to', placeholder="Friend's email"),
            Field('comment', rows="4"),
            Row(
                Div(
                    Submit('submit', 'Send message'),
                    HTML('<a class="btn btn-secondary" href="'+ kwargs['initial']['url'] +'">Cancel</a>'),
                    css_class="col text-center form-buttons" 
                )
            ),
            Field('url', type="hidden")
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {'body': 'Comment'}

    def __init__(self, **kwargs):
        super(CommentForm, self).__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('body', rows=4),
            Row(
                Div(
                    Submit('submit', 'Send message'),
                    css_class="col text-center form-buttons" 
                )
            )
        )

class SearchForm(forms.Form):
    query = forms.CharField()