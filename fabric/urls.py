from django.conf.urls import patterns, include, url

from fabric import views

urlpatterns = patterns('',
    url(r'^$', views.FrontPageView, name='frontpage'),
    # url(r'^monthlykickstart/$', views.MonthlyKickStartPageView, name='monthlykickstart'),
    # url(r'^monthlyvp/$', views.MonthlyvpPageView, name='monthlyvp'),
    # url(r'^kickstartedition/$', views.FirstStagePageView, name='kickstartedition'),
    # url(r'^kseresource/$', views.ResourcePageView, name='kseresource'),
    # url(r'^ksenumbers/$', views.NumbersPageView, name='ksenumbers'),
    url(r'^errorpage/$', views.ErrorPageView, name='errorpage'),
    url(r'^cfcalc/$', views.CfCalcView, name='cfcalcpage'),
)
