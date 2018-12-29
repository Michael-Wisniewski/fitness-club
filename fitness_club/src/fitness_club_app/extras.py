from django.http import HttpResponseBadRequest

class Section():
    section = ''

    def get_context_data(self, **kwargs):
        context = super(Section, self).get_context_data(**kwargs)
        context['section'] = self.section
        return context

class AjaxRequired():

    def dispatch(self, *args, **kwargs):
        if self.request.is_ajax():
            return super(AjaxRequired, self).dispatch(*args, **kwargs)
        else:
            return HttpResponseBadRequest()