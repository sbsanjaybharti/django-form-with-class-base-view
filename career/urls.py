from django.conf.urls import url

from career.views import CareerCreate, CareerUpdate

urlpatterns = [
    url(r'^$', CareerCreate.as_view(), name='career_create'),
    url(r'^(?P<pk>\d+)/edit/$', CareerUpdate.as_view(), name='career_update'),
]