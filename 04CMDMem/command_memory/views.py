from django.views.generic import ListView
from .models import commandmem

class IndexPageView(ListView):
    model = commandmem
    template_name = 'index.html'
