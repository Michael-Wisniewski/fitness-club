from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from django.views.generic import TemplateView, CreateView
from .models import SliderPicture
from django.core.urlresolvers import reverse_lazy
from .forms import SlideForm


class SlidesListView(Section, EmployeeLoginRequired, TemplateView):
    template_name = 'slider_backend/slides_list.html'

    def get_context_data(self, **kwargs):
        context = super(SlidesListView, self).get_context_data(**kwargs)
        context['slides'] = SliderPicture.objects.all().order_by('order')
        return context

class SlideCreateView(Section, EmployeeLoginRequired, CreateView):
    template_name = 'slider_backend/slide_create.html'
    model = SliderPicture
    form_class = SlideForm
    success_url = reverse_lazy('slider_backend:slides_list')
    max_order = SliderPicture.objects.all().count() + 1
    initial = {'cancel_url': reverse_lazy('slider_backend:slides_list'),
               'max_order': max_order}

    def form_valid(self, form):
        form.update_order_values()
        return super(SlideCreateView, self).form_valid(form)