from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from django.views.generic import TemplateView, CreateView, View, DeleteView
from .models import SliderPicture
from django.core.urlresolvers import reverse_lazy
from .forms import SlideForm
from fitness_club_app.extras import AjaxRequired
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect

class SlidesListView(Section, EmployeeLoginRequired, TemplateView):
    template_name = 'slider_backend/slides_list.html'

    def get_context_data(self, **kwargs):
        context = super(SlidesListView, self).get_context_data(**kwargs)
        context['slides'] = SliderPicture.objects.all()
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

class UpdateSlidesOrder(EmployeeLoginRequired, AjaxRequired, View):

    def post(self, request):
        operation_status = ''
        slide_id = int(request.POST['slide_id'])
        slide_order = int(request.POST['slide_order'])
        
        try:
            slide_obj = SliderPicture.objects.get(id=slide_id)
            original_order = slide_obj.order
            slide_obj.order = slide_order
            slide_obj.save()

            if slide_order < original_order:
                slides_to_update = SliderPicture.objects.filter(order__gte=slide_order, order__lt=original_order).exclude(id=slide_obj.id)
                for slide in slides_to_update:
                    slide.order += 1
                    slide.save()
            else:
                slides_to_update = SliderPicture.objects.filter(order__gt=original_order, order__lte=slide_order).exclude(id=slide_obj.id)
                for slide in slides_to_update:
                    slide.order -= 1
                    slide.save()

            operation_status = 'OK'
        except SliderPicture.DoesNotExist:
            operation_status = 'No such slide in database.'
            pass

        data = {'operation_status': operation_status}
        return JsonResponse(data)

class SlideDeleteView(Section, EmployeeLoginRequired, DeleteView):
    template_name = 'slider_backend/slide_delete.html'
    model = SliderPicture
    success_url = reverse_lazy('slider_backend:slides_list')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            deleted_obj = SliderPicture.objects.get(id=kwargs['pk'])
            deleted_order = deleted_obj.order
            slides_to_update = SliderPicture.objects.filter(order__gt=deleted_order)

            for slide in slides_to_update:
                slide.order -= 1
                slide.save()
            
            return super(SlideDeleteView, self).post(request, *args, **kwargs)