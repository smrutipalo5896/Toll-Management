from django.conf.urls import url
from . import views
urlpatterns=[
    #/emp/
    url(r'^$',views.index,name='index'),
    
    #/music/32/
    url(r'^(?P<employeeId>[0-9]+)/',views.detail,name='detail'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),

    
    ]
