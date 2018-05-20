from django.conf.urls import url,patterns,include
from . import views
from profiles.views import userProfile
urlpatterns=[
    url(r'^$',views.homee,name='homee'),
    url(r'^about/',views.aboutsm,name='aboutsm'),
    url(r'^profiles/$',userProfile.as_view(),name='userProfile'),
    url(r'^FAQ/',views.faqsm,name='faqsm'),


    ]