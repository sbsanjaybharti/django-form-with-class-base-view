from django import forms

from career.models import Career


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields =[
            'user',
            'position',
            'responsibility',
            'current_working',
            'start_month',
            'start_year',
            'end_month',
            'end_year',
            'company_type',
            'company_name',
            'location'
        ]