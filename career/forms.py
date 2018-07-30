from django import forms

from career.models import Career
from django.utils.translation import gettext_lazy as _


class CareerFormWithFormValidation(forms.ModelForm):
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
    def clean(self):
        cleaned_data = super(CareerFormWithFormValidation, self).clean()
        if(cleaned_data['position'] == None):
            raise forms.ValidationError(_('Error! Position is required'))
        if(cleaned_data['responsibility'] == None):
            raise forms.ValidationError(_('Error! Responsibility is required'))
        if(cleaned_data['current_working'] == None):
            raise forms.ValidationError(_('Error! Current working is required'))
        if(cleaned_data['start_month'] == None):
            raise forms.ValidationError(_('Error! Start month is required'))
        if(cleaned_data['start_year'] == None):
            raise forms.ValidationError(_('Error! Start year is required'))
        if(cleaned_data['end_month'] == None):
            raise forms.ValidationError(_('Error! End month is required'))
        if(cleaned_data['end_year'] == None):
            raise forms.ValidationError(_('Error! End year is required'))
        if(cleaned_data['company_type'] == None):
            raise forms.ValidationError(_('Error! Company type is required'))
        return cleaned_data

class CareerFormWithFieldValidation(forms.ModelForm):
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
    def clean_position(self):
        data = self.cleaned_data['position']
        if(data == None):
            raise forms.ValidationError('Error! Position is required')
        else:
            return data

    def clean_responsibility(self):
        data = self.cleaned_data['responsibility']
        if(data == None):
            raise forms.ValidationError('Error! Responsibility is required')
        else:
            return data

    def clean_end_month(self):
        data = self.cleaned_data['end_month']
        if(data == None):
            raise forms.ValidationError('Error! End month is required')
        else:
            return data

    def clean_start_year(self):
        data = self.cleaned_data['start_year']
        if(data == None):
            raise forms.ValidationError('Error! Start year is required')
        if int(data) < 1900:
            raise forms.ValidationError('Start year is invalid')
        else:
            return data

    def clean_end_year(self):
        data = self.cleaned_data['end_year']
        if(data == None):
            raise forms.ValidationError('Error! End year is required')
        if int(data) < 1900:
            raise forms.ValidationError('End year is invalid')
        else:
            return data

    def clean_company_type(self):
        data = self.cleaned_data['company_type']
        if(data == None):
            raise forms.ValidationError('Error! Company type is required')
        else:
            return data

    def clean_company_name(self):
        data = self.cleaned_data['company_name']
        if(data == None):
            raise forms.ValidationError('Error! Company name is required')
        else:
            return data

    def clean_location(self):
        data = self.cleaned_data['location']
        if(data == None):
            raise forms.ValidationError('Error! Location is required')
        else:
            return data