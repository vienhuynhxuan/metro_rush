from django.shortcuts import render
from django.views import generic
# Create your views here.

class RequestView(generic.ListView):
    template_name = 'index.html'
    
    def get_queryset(self):
        return None
