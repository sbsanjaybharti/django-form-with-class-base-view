from django.contrib import messages
from django.forms import Form
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from career.forms import CareerForm
from career.models import Career


class CareerCreate(CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'career/create.html'
    context_object_name = "career"
    def get_object(self, queryset=None):
        try:
            career = Career.objects.get(id=1)
        except:
            career = None
        return career
    def post(self, request, *args, **kwargs):
        form = CareerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('career_update', kwargs={'pk': form.instance.id}))
        return render(request, self.template_name, {'form': form})

class CareerUpdate(UpdateView):
    model = Career
    form_class = CareerForm
    template_name = 'career/create.html'
    context_object_name = "form"
    def post(self, request, *args, **kwargs):
        server = get_object_or_404(Career, pk=kwargs['pk'])
        form = CareerForm(request.POST or None, instance=server)
        if form.is_valid():
            form.save()
            return redirect(reverse('career_update', kwargs={'pk': form.instance.id}))
        else:
            return render(request, self.template_name, {'form': form})