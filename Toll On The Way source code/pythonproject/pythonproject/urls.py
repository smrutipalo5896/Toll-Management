from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin
from contact import  views as contact_views
from profiles import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emp/', include('emp.url')),
    url(r'^toll/',include('toll.urls')),
    url(r'^contact/$',contact_views.contact,name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^', include('pay.urls')),
  
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)