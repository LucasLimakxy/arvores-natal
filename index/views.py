from django.shortcuts import render
from django.views.generic import ListView
from index.models import *

# Create your views here.
class DashboardView(ListView):
    model = Familia
    template_name = 'index/familia_list.html'