from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^frontpage/', include('fabric.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

handler404 = 'fabric.views.handlerCustom404'
handler500 = 'fabric.views.handlerCustom500'