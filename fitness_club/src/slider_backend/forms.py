from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, HTML, Field, Submit
from slider_backend.models import SliderPicture

class SlideForm(forms.ModelForm):
    class Meta:
        model = SliderPicture
        fields = ('image', 'order')

    def __init__(self, **kwargs):
        super(SlideForm, self).__init__(**kwargs)
        cancel_url = kwargs['initial']['cancel_url']
        max_order = kwargs['initial']['max_order']
        choices = [(i,i) for i in range(1, (max_order+1))]
        self.fields['order'] = forms.ChoiceField(widget=forms.Select(),
                                                 choices=choices)
        self.initial['order'] = max_order
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2'
        self.helper.layout = Layout(
            Field('image'),
            Field('order'),
            ButtonHolder(
                Submit('submit', 'Submit'),
                HTML("<a class='btn btn-secondary' href='{}'>Cancel</a>".format(cancel_url))
            )
        )

    def update_order_values(self):
        order = int(self.cleaned_data['order'])
        flag = True
        slider = None 
        temp_slider = None

        while flag:
            try:
                if temp_slider is None:
                    slider = SliderPicture.objects.get(order=order)
                else:
                    slider = temp_slider
                order += 1
                temp_slider = SliderPicture.objects.get(order=(order))
                slider.order = order
                slider.save()
            except SliderPicture.DoesNotExist:
                if slider is not None:
                    slider.order = order
                    slider.save()
                flag = False 
        pass