from django.test import TestCase
from SiteUsers.models import UserProfile,Friends,Education,Location,School
from django.contrib.auth.models import User
import requests
from django.conf import settings
# allen and kelvin went to same uni, live in different cities
# check entry into DB and relationships
# check that friends from either end

test_uni = {'school_name':'University of Melbourne','school_id':'idunimelb','school_type':'College'}
test_hs = {'school_name':'Merrilands HS','school_id':'idmerrilands','school_type':'HS'}
test_location_a = {'location_id':'123Melb','location_name':'Melbourne, Australia'}
test_location_b = {'location_id':'888Syd','location_name':'Sydney, Australia'}
test_userprofile_a = {'first_name':'Allen','last_name':'Tran','fb_token':'FBatran','ig_token':'IGatran',
             'ig_username':'realallentran','ig_pic':'http://ig.com/atranman.jpg','ig_follows':1,
             'ig_followers':100,'birthyear':1984,'gender':'Male'
             }
test_userprofile_b = {'first_name':'Kelvin','last_name':'Tran','fb_token':'FBktran','ig_token':'IGktran',
             'ig_username':'mememelookatme','ig_pic':'http://ig.com/ktranman.jpg','ig_follows':0,
             'ig_followers':1010,'birthyear':1984,'gender':'Male'
             }
test_user_a = {'username':'user_a','password':'password','email':'email'}
test_user_b = {'username':'user_b','password':'password','email':'email@email.com'}

class DBTestCase(TestCase):
  # or load fixtures from DB
  def createdata(self):
    location_a = Location.objects.create(**test_location_a)
    location_b = Location.objects.create(**test_location_b)
    Uni = School.objects.create(**test_uni)
    HS = School.objects.create(**test_hs)

    user_a = User.objects.create_user(**test_user_a)
    userprofile_a = UserProfile.objects.create(user=user_a,location=location_a,**test_userprofile_a)

    user_b = User.objects.create_user(**test_user_b)
    userprofile_b = UserProfile.objects.create(user=user_b,location=location_b,**test_userprofile_b)

    Education.objects.create(user=userprofile_a,school=Uni)
    Education.objects.create(user=userprofile_b,school=Uni)
    Education.objects.create(user=userprofile_a,school=HS)
    Friends.objects.create(person=userprofile_a,friend=userprofile_b)
    Friends.objects.create(person=userprofile_b,friend=userprofile_a)
    return user_a,user_b,userprofile_a,userprofile_b

  def test_checkExists(self):
    user_a,user_b,userprofile_a,userprofile_b = self.createdata()
    users_a = User.objects.filter(username=test_user_a['username']).count()
    users_b = User.objects.filter(username=test_user_b['username']).count()
    return self.assertTrue((users_a>0) & (user_b >0))
  
  def test_checkLocationRelationship(self):
    self.createdata()
    Melbourne = UserProfile.objects.filter(location__location_id='123Melb').count()
    return self.assertEqual(Melbourne,1)

  def test_checkEducationRelationship(self):
    user_a,user_b,userprofile_a,userprofile_b = self.createdata()
    UMelb = UserProfile.objects.filter(education__school_id='idunimelb')
    return self.assertTrue( (userprofile_a in UMelb) & (userprofile_b in UMelb) )

  def test_checkFriendsRelationship(self):
    user_a,user_b,userprofile_a,userprofile_b = self.createdata()
    AFriends = userprofile_a.getFriendsList()
    BFriends = userprofile_b.getFriendsList()
    return self.assertTrue( (userprofile_a in BFriends) & (userprofile_b in AFriends) )
    
# Connect to instagram, connect to FB
class FBIGTests(TestCase):

  def test_IG(self):
    r = requests.get('https://api.instagram.com/v1/media/popular?client_id='+settings.IG_CLIENT_ID)
    return self.assertEqual(r.status_code,200)

  def test_FB(self):
    # need to get new access token before running test
    access_token = 'CAALXlVGl6aABAKyhbDSZC8TtUOUgsaHaswV149TIV0hEFHhlPDIU8vRatI7EXvHrzxKowMFpv8X1pckBI2r7xnRMDkekbq1ZCVPs8Mmozy56xZAYnB42Vj8y1FKbe1RS4lEAgVUlZArItWSoWc9GNkmBER3m6WayKgkxQaZAXMHJckfx5ifBL2iTzsblwbXvkpO4nD3wphAZDZD'
    r = requests.get('https://graph.facebook.com/v2.0/me?access_token='+access_token)
    return self.assertEqual(r.json()['name'],'Open Graph Test User')

