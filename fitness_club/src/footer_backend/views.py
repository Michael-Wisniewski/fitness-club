from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from django.views.generic import FormView
from .forms import FooterForm
from django.core.urlresolvers import reverse_lazy
import fileinput

class FooterDataView(Section, EmployeeLoginRequired, FormView):
    template_name = 'footer_backend/footer_data.html'
    form_class = FooterForm
    success_url = reverse_lazy('footer_backend:footer_data')

    def form_valid(self, form):
        cd = form.cleaned_data
        cd['about_us'] = "<br/>".join(cd['about_us'].splitlines())
        data_file = fileinput.input("/fitness_club/src/footer_backend/data.txt", inplace=True)

        for line in data_file :
            line_arr = line.split(" ", 1)
            field = line_arr[0]
            line = "{} {}".format(field, cd[field])
            print(line)
        
        data_file.close()

        return super(FooterDataView, self).form_valid(form)