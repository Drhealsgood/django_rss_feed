from django.db import models
import re
import feedparser

# Create your models here.
class Feed(models.Model):
    name    = models.CharField(max_length=50)
    url     = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Feed_Item(models.Model):    
    feed = models.ForeignKey(Feed)
    link = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title
