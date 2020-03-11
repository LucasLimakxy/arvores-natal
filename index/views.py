from django.shortcuts import render
from django.views.generic import ListView, DetailView
from index.models import *

# Create your views here.
class DashboardView(ListView):
    model = Familia
    template_name = 'index/dashboard.html'

class ListArvoresView(DetailView):
    model = Familia
    template_name = 'index/arvores_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['arvores'] = Arvore.objects.filter(familia=self.get_object())
        return context