from django.contrib import messages
from django.forms import Form
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from career.forms import CareerFormWithFormValidation, CareerFormWithFieldValidation
from career.models import Career
from django.utils.translation import gettext_lazy as _

def home(request):
        return render(request, 'career/home.html')

class CareerCreate(CreateView):
    model = Career
    form_class = CareerFormWithFormValidation
    template_name = 'career/create.html'
    context_object_name = "career"
    def get_object(self, queryset=None):
        try:
            career = Career.objects.get(id=1)
        except:
            career = None
        return career
    def post(self, request, *args, **kwargs):
        form = CareerFormWithFormValidation(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, _('Sucess! Data saved sucessfully'))
                return redirect(reverse('career_update', kwargs={'pk': form.instance.id}))
            except:
                messages.error(request, _('Some thing went wrong try again.'))
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, _('Error! Invalid form'))
            return render(request, self.template_name, {'form': form})

class CareerCreateTwo(CreateView):
    model = Career
    form_class = CareerFormWithFieldValidation
    template_name = 'career/create_field_validation.html'
    context_object_name = "career"
    def get_object(self, queryset=None):
        try:
            career = Career.objects.get(id=1)
        except:
            career = None
        return career
    def post(self, request, *args, **kwargs):
        form = CareerFormWithFieldValidation(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, _('Sucess! Data saved sucessfully'))
                return redirect(reverse('career_update', kwargs={'pk': form.instance.id}))
            except:
                messages.error(request, _('Some thing went wrong try again.'))
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, _('Error! Invalid form'))
            return render(request, self.template_name, {'form': form})

class CareerUpdate(UpdateView):
    model = Career
    form_class = CareerFormWithFormValidation
    template_name = 'career/create.html'
    context_object_name = "form"
    def post(self, request, *args, **kwargs):
        server = get_object_or_404(Career, pk=kwargs['pk'])
        form = CareerFormWithFormValidation(request.POST or None, instance=server)
        if form.is_valid():
            form.save()
            return redirect(reverse('career_update', kwargs={'pk': form.instance.id}))
        else:
            return render(request, self.template_name, {'form': form})