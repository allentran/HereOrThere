from django.test import TestCase
from SiteUsers.models import UserProfile,Friends,Education,Location,School
from django.contrib.auth.models import User
# Create a user, userprofile, education (linked), school, location (linked), another user and userprofile and relationship
# Get user A's details + friends

test_uni = School(school_name='University of Melbourne',school_id='idunimelb',school_type='College')
test_hs = School(school_name='Merrilands HS',school_id='idmerrilands',school_type='HS')
test_location_a = Location(location_id='123Melb',location_name='Melbourne, Australia')
test_location_b = Location(location_id='888Syd',location_name='Sydney, Australia')
test_user_a = {'first_name':'Allen','last_name':'Tran','fb_token':'FBatran','ig_token':'IGatran',
             'ig_username':'realallentran','ig_pic':'http://ig.com/atranman.jpg','ig_follows':1,
             'ig_followers'=100,'location':test_location_a,'birthyear':1984,'gender':'Male'
             }
test_user_b = {'first_name':'Kelvin','last_name':'Tran','fb_token':'FBktran','ig_token':'IGktran',
             'ig_username':'mememelookatme','ig_pic':'http://ig.com/ktranman.jpg','ig_follows':0,
             'ig_followers'=1010,'location':test_location_b,'birthyear':1984,'gender':'Male'
             }

class DBTestCase(TestCase):
  # or load fixtures from DB
  def setup(self):
    user_a = User(username='user_a',password='password',email='email')
    userprofile_a = UserProfile(user=user_a,**test_user_a)
    user_b = User(username='user_b',password='password',email='email@email.com')
    userprofile_b = UserProfile(user=user_b,**test_user_b)

    user_a.save(),user_b.save()
    userprofile_a.save(),userprofile_b.save()

  def checkExists(self):
    users = User.objects.all()
    return self.assertIn(user_a,users)
    
# Connect to instagram, connect to FB
#class FBTestCase(TestCase):


