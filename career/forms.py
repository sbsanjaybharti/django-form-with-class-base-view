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
    def clean(self):
        cleaned_data = super(CareerForm, self).clean()
        if int(cleaned_data.get('start_year')) < 1900:
            raise forms.ValidationError('Start year is invalid')
        if int(cleaned_data.get('end_year')) < 1900:
            raise forms.ValidationError('End year is invalid')
        return cleaned_data

