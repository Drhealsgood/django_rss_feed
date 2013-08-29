from django.db import models
import feedparser

# Create your models here.
"""
add a feed
Feed().create(feed['feed']['title'],feed['href'],feed['feed']['link'])
"""

class Feed(models.Model):
    name    = models.CharField(max_length=50)
    feed_url= models.CharField(max_length=100)
    url     = models.CharField(max_length=100)
    
    @classmethod
    def create(cls, ititle, furl, iurl):
        feed = cls(name=ititle,feed_url=furl,url=iurl)
        return feed
        
    def get_feed(self):
        parsed = feedparser.parse(self.feed_url)
        for entry in parsed['entries']:
            yield entry
    
    def __unicode__(self):
        return self.name
        
    def __str__(self):
        return self.name
        
class Feed_Item(models.Model):
    feed    = models.ForeignKey('Feed')
    title   = models.CharField(max_length=50)
    url     = models.CharField(max_length=100)
    content = models.CharField(max_length=999)
    
    @classmethod
    def create(cls, feed):
        feed_entries = feed.get_feed()
        feed_entry   = next(feed_entries)
        obj = cls(feed=feed, title=feed_entry['title'],url=feed_entry['links'][0]['href'],
                    content=feed_entry['content'][0]['value'])
        return obj
        
    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title
    
    
