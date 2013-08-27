from django.conf.urls import patterns, url

from rss_feed import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<feed_title>\d+)/$', views.feed_results, name="feed_results"),
)
   
