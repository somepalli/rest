from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from master import views
from django.contrib.auth.decorators import login_required
import debug_toolbar
urlpatterns = patterns('',
  # url(r'^login/$','django.contrib.auth.views.login',name='login',kwargs={'template_name': 'master/login.html'}),
  # url(r'^logout/$','django.contrib.auth.views.logout',name='logout',kwargs={'next_page': '/master/login'}),
  
  # url(r'^home/$','master.views.home', name='home'),
  # url(r'^accounts/login/$', auth_views.login),
  # url(r'^master/login/$', auth_views.login),
  url(r'^users/$', views.MasterRepaymentList.as_view()),
  # url(r'^addmasterchannel/$','master.views.addmasterchannel', name='addmasterchannel'),
  url(r'^users/(?P<pk>[0-9]+)/$', views.MasterRepaymentDetail.as_view()),
  url(r'^__debug__/', include(debug_toolbar.urls)),
  # url(r'^channeledit/(?P<pk>\d+)$', views.MasterChannelUpdate.as_view(), name='masterchannel_edit'),
  # url(r'^channeldelete/(?P<pk>\d+)$', views.MasterChannelDelete.as_view(), name='masterchannel_delete'),
  # url(r'^submitrecipe/$','master.views.submit_recipe', name='submitrecipe'),
  # url(r'^create/$','master.views.create', name='create'),
  # url(r'^addclient/$','master.views.addclient', name='addclient'),
 
)