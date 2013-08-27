# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from rss_feed.models import Feed

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
    
def feed_results(request, feed_title):
    return HttpResponse("You're look at feed {0}".format(feed_title))
