from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from career.forms import CareerForm
from career.models import Career


class CareerCreate(CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'career/create.html'
    def get_object(self, queryset=None):
        try:
            career = Career.objects.get(id=self.request.GET.get('id'))
        except:
            career = None
        return career