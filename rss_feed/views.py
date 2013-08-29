# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from rss_feed.models import Feed

import feedparser



def index(request):
    """
    index lists the feeds we are tracking
    """
    feed_list = Feed.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'feed_list': feed_list,
    })
    return HttpResponse(template.render(context))
    
def feed_results(request, feed):
    """
    feed_results returns the results of given feed
    """
    results = feedparser.parse(feed_url)
    template = loader.get_template('feed_results.html')
    context = RequestContext(request, {
        'title'  : results['feed']['title'],
        'url'    : results['feed']['link'],
        'entries': results['entries']
    })
    return HttpResponse(template.render(context))
