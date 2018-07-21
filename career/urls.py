from django.conf.urls import url

from career.views import CareerCreate

urlpatterns = [
    url(r'^$', CareerCreate.as_view(), name='career_create'),
]