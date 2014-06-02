from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	fb_token = models.CharField(max_length=500)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	fb_id = models.CharField(max_length=200,primary_key=True)
	ig_token = models.CharField(max_length=500,default='')
	location = models.ForeignKey('Location')
	birthyear = models.CharField(max_length=200)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

	def fullname(self):
		return self.first_name +' ' + self.last_name

class Friends(models.Model):
	person = models.ForeignKey('UserProfile',related_name='person')
	friend = models.ForeignKey('UserProfile',related_name='friend')
	class Meta:
		unique_together = (("person", "friend"),)
	def __unicode__(self):
		return self.person.fullname(),self.friend.fullname()

class Education(models.Model):
	user = models.ForeignKey('UserProfile')
	school = models.ForeignKey('School')
	def __unicode__(self):
		return self.user.fullname() + ' ' + self.school.school_name

class Location(models.Model):
	location_id = models.CharField(max_length=200,primary_key=True)
	location_name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.location_name

class School(models.Model):
	school_id = models.CharField(max_length=200,primary_key=True)
	school_name = models.CharField(max_length=200)
	school_type = models.CharField(max_length=200)
	def __unicode__(self):
		return self.school_name