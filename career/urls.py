from django.conf.urls import url

from career.views import CareerCreate, CareerUpdate, CareerCreateTwo

urlpatterns = [
    url(r'^form/validation/$', CareerCreate.as_view(), name='career_create_form_validation'),
    url(r'^form/field/validation/$', CareerCreateTwo.as_view(), name='career_create_form_field_validation'),
    url(r'^(?P<pk>\d+)/edit/$', CareerUpdate.as_view(), name='career_update'),
]