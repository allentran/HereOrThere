from django.db import models
from django.conf import settings

import requests

from SiteUsers.models import UserProfile,Friends,Education,School


class Bar(models.Model):
    FS_id = models.CharField(primary_key=True,max_length=255)
    IG_id = models.CharField(max_length=255)
    Name = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __unicode__(self):
        return self.Name

    def GetIG_ID(self):
        IG_URL = 'https://api.instagram.com/v1/locations/search?foursquare_v2_id=' + self.FS_id + '&v=20140226&client_id='+settings.IG_CLIENT_ID+'&client_secret='+settings.IG_CLIENT_SECRET
        r = requests.get(IG_URL)
        if len(r.json()['data']) > 0:
            self.IG_id = r.json()['data'][0]['id']
            self.save()
        else:
            self.IG_id = ''
            self.save()



class BarLocations(models.Model):
    bar = models.ForeignKey(Bar)
    neighborhood = models.ForeignKey('SiteUsers.Neighborhood')
    distance = models.FloatField(default=0)

class PublicLadder(models.Model):
    city = models.ForeignKey('SiteUsers.City') # namespacing models?
    date = models.DateField()

class PublicOrdering(models.Model):
    ladder = models.ForeignKey('PublicLadder')
    bar = models.ForeignKey(Bar)
    rank = models.IntegerField()

class Vote(models.Model):
    user = models.ForeignKey('SiteUsers.UserProfile')
    winner = models.ForeignKey(Bar,related_name='winner',null=True)
    loser = models.ForeignKey(Bar,related_name='loser',null=True)
    date = models.DateField()

class IGrank(models.Model):
    date = models.DateField()
    bar = models.ForeignKey(Bar)
    total_likes = models.IntegerField()
    avg_likes = models.FloatField()

class Bar(models.Model):
	FS_id = models.CharField(primary_key=True,max_length=255)

class PublicLadder(models.Model):
	location = models.ForeignKey('SiteUsers.Location') # namespacing models?
	date = models.DateField()

class PublicOrdering(models.Model):
	ladder = models.ForeignKey('PublicLadder')
	bar = models.ForeignKey('bar')
	rank = models.IntegerField()

class Vote(models.Model):
	user = models.ForeignKey('SiteUsers.UserProfile')
	winner = models.ForeignKey('Bar',related_name='winner')
	loser = models.ForeignKey('Bar',related_name='loser')
	date = models.DateField()

class IGrank(models.Model):
	date = models.DateField()
	bar = models.ForeignKey(Bar)
	total_likes = models.IntegerField()
	avg_likes = models.FloatField()





