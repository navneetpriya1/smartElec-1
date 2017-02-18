from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartElecAdmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard$','main.views.dashboard',name='dashboard'),
    url(r'^table$','main.views.table',name='table'),
    url(r'^notifications$','main.views.notifications',name='notifications'),
    url(r'^typography$','main.views.typography',name='typography'),
    url(r'^start$','main.views.start',name='start'),
)