from django.conf.urls import url
from . import views
urlpatterns=[
    #/emp/
    url(r'^$',views.contact,name='contact'),


    
    ]
