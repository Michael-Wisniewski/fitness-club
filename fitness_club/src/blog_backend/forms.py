from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, HTML, Button, Div
from blog.models import Post
from account.models import User
from PIL import Image

class PostForm(forms.ModelForm):
    x = forms.IntegerField(required=False)
    y = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)

    class Meta: 
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'publish', 'status', 'image', 'x')
        widgets = {
            'image': forms.FileInput,
        }

    def __init__(self, **kwargs):
        super(PostForm, self).__init__(**kwargs)
        cancel_url = kwargs['initial']['cancel_url']
        self.fields['author'].queryset = User.objects.filter(is_active=True, is_employee=True)
        self.fields['author'].empty_label = None
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
            ),
            Field('x', type='hidden'),
            Field('y', type='hidden'),
            Field('width', type='hidden'),
            Field('height', type='hidden')
        )

    def save(self):
        post = super(PostForm, self).save()
        cd = self.cleaned_data
        x = cd['x']
        y = cd['y']
        w = cd['width']
        h = cd['height']

        if (x and y and w and h) is not None:
            image = Image.open(post.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((750, 500), Image.ANTIALIAS)
            imagePath = post.image.path
            resized_image.save(post.image.path)
          
        return post

