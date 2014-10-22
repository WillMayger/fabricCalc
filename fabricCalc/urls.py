from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('fabric.urls')),
    #(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),


)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'fabric.views.handlerCustom404'
handler500 = 'fabric.views.handlerCustom500'