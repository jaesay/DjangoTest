from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
    #url(r'^polls/$', views.index, name='index'),
    #url(r'^polls/(?P<question_id>\d+)/$', views.detail, name = 'detail'),
    #url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^polls/(?P<question_id>\d+)/result/$', views.results, name='results'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', views.search),
)
