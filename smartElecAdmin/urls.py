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
    url(r'^weather$', 'main.views.datagerator', name='datagerator') , #giving 3 coordinates, 
    url(r'^idealsurplus$', 'main.views.ideal_surplus', name='realgenerator') , #giving ideal surplus ammount for the day

    url(r'^deviceinfo$', 'main.views.deviceInfo',name="deviceInfo"),
    url(r'^userinfo$', 'main.views.userInfo',name="userInfo"),

    url(r'^exactprice$', 'main.views.exactPrice',name="exactprice"), #exact price at the moment
    url(r'^idealrate$', 'main.views.exact',name="exact"),#giving ideal minimum price for comparison

)
