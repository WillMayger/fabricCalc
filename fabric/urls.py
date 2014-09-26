from django.conf.urls import patterns, include, url

from fabric import views

urlpatterns = patterns('',
    url(r'^$', views.FrontPageView, name='frontpage'),
    url(r'^monthlykickstart/$', views.MonthlyKickStartPageView, name='monthlykickstart'),
    url(r'^monthlyvp/$', views.MonthlyvpPageView, name='monthlyvp'),
    url(r'^kickstartedition/$', views.KickStarterPageView, name='kickstartedition'),
    url(r'^virtualprivateedition/$', views.VirtualPrivatePageView, name='virtualprivateedition'),
    url(r'^kseresource/$', views.KSResourcePageView, name='kseresource'),
    url(r'^ksenumbers/$', views.KSNumbersPageView, name='ksenumbers'),
    url(r'^vperesource/$', views.VPResourcePageView, name='vperesource'),
    url(r'^vpenumbers/$', views.VPNumbersPageView, name='vpenumbers'),
    url(r'^errorpage/$', views.ErrorPageView, name='errorpage'),
)
