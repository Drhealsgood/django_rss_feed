from django.db import models

# Create your models here.
class Feed(models.Model):
    name    = models.CharField(max_length=50)
    url     = models.CharField(max_length=50)
    
    @classmethod
    def create(cls, ititle, iurl):
        feed = cls(name=ititle,url=iurl)
        return feed
    
    def __unicode__(self):
        return self.name
        
    def __str__(self):
        return self.name
    
class Feed_Item(models.Model):    
    feed = models.ForeignKey(Feed)
    link = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title
