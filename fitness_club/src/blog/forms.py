from django import forms
from django.core.mail import send_mail

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)
    title = forms.CharField()
    url = forms.CharField()

    def send_email(self):
        cd = self.cleaned_data
        subject = '{} ({}) invites you to read "{}"'.format(cd['name'], cd['email'], cd['title'])
        message = 'You can read post "{}", by clicking on the link below:\n\n{}\n\nComment added by {}.'\
                  .format(cd['title'], cd['url'], cd['name'], cd['comment'])        
        send_mail(subject, message, 'info@fitnessclub.pl', [cd['to']])
        pass                

