from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User,primary_key=True)
  fb_token = models.CharField(max_length=500)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  fb_id = models.CharField(max_length=200,default='')
  ig_token = models.CharField(max_length=500,default='')
  ig_username = models.CharField(max_length=100,default='')
  ig_pic = models.CharField(max_length=100,default='')
  ig_follows = models.IntegerField(default=0)
  ig_followers = models.IntegerField(default=0)
  city = models.ForeignKey('City',null=True)
  birthyear = models.IntegerField()
  gender = models.CharField(max_length=10,default='')

    # Override the __unicode__() method to return out something meaningful!
  def __unicode__(self):
    return self.user.username

  def fullname(self):
    return self.first_name +' ' + self.last_name

  # def getFriendsList(self):
  #   return UserProfile.objects.filter(friend__person=self)

  def isMale(self):
    return self.user.userprofile.gender == 'Male'

class Friends(models.Model):
  person = models.ForeignKey('UserProfile',related_name='person')
  friend = models.ForeignKey('UserProfile',related_name='friend')
  class Meta:
    unique_together = (("person", "friend"),)
  def __unicode__(self):
    return self.person.fullname() + ' is friends with ' + self.friend.fullname()

class Education(models.Model):
  user = models.ForeignKey('UserProfile')
  school = models.ForeignKey('School')
  def __unicode__(self):
    return self.user.fullname() + ' went to ' + self.school.school_name

class City(models.Model):
  city_name = models.CharField(max_length=200)
  state = models.CharField(max_length=50)
  def __unicode__(self):
    return self.city_name

class Neighborhood(models.Model):
  neighborhood_name = models.CharField(max_length=200)
  city = models.ForeignKey('SiteUsers.City')
  lat = models.FloatField(default=0)
  lng = models.FloatField(default=0)
  bars_last_updated = models.DateField()
  
  def __unicode__(self):
    return self.neighborhood_name


class School(models.Model):
  school_id = models.CharField(max_length=200,primary_key=True)
  school_name = models.CharField(max_length=200)
  school_type = models.CharField(max_length=200)
  def __unicode__(self):
    return self.school_name