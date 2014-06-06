from django.db import models
from SiteUsers.models import UserProfile,Friends,Education,Location,School
from django.contrib.auth.models import User
# These should be updated at intervals or saved when a user requests one

# each location may have at most a single public ranking

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
	user = models.ForeignKey(User)
	winner = models.ForeignKey('Bar',related_name='winner')
	loser = models.ForeignKey('Bar',related_name='loser')
	date = models.DateField()

	def isMale(self):
		return self.user.userprofile.gender == 'Male'



