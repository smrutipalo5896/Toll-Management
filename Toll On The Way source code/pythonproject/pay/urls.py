from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^pay/',views.pay,name='pay')
    ]