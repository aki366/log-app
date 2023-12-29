from django.views.generic import ListView
from .models import Careerlog

class CareerlogListView(ListView):
    model = Careerlog
    template_name = 'careerlog_list.html'
    context_object_name = 'careerlogs'
