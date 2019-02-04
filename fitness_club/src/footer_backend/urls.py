from django.conf.urls import url
from . import views

module_name = 'footer_backend'

urlpatterns = [
    url(r'^footer_data/$',
            views.FooterDataView.as_view(section=module_name),
            name='footer_data')
]