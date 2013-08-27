from django.db import models

# Create your models here.
"""
add a feed
Feed().create(feed['feed']['title'],feed['href'],feed['feed']['link'])
"""

class Feed(models.Model):
    name    = models.CharField(max_length=50)
    feed_url= models.CharField(max_length=50)
    url     = models.CharField(max_length=50)
    
    @classmethod
    def create(cls, ititle, furl, iurl):
        feed = cls(name=ititle,feed_url=furl,url=iurl)
        return feed
    
    def __unicode__(self):
        return self.name
        
    def __str__(self):
        return self.name
    
