from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from SiteUsers.models import UserProfile,Friends,Education,Location,School
import requests

# update ig_data for userprofile
def updateIGdata(userprofile,userdata):
  token = userprofile.ig_token
  userprofile.ig_username = userdata['username']
  userprofile.ig_pic = userdata['profile_picture']
  if 'counts' in userdata:
    userprofile.ig_follows = userdata['counts']['follows']
    userprofile.ig_followers = userdata['counts']['followed_by']
  userprofile.save()

# Check if current token is valid by trying to update
def check(request):
  state = request.GET.get("state")
  stored_token = request.user.userprofile.ig_token
  r = requests.get('https://api.instagram.com/v1/users/self?access_token='+stored_token).json()
  if r['meta']['code'] == 200:
    updateIGdata(request.user.userprofile,r['data'])
    return HttpResponse('IG all good + updated, should be battle or location')
  else: #go login and get a new token
    return HttpResponseRedirect(reverse('SiteUsers:instagram')+'?state='+state)

# Return HttpRedirect based on state

def getRedirectURL(state):
  if state == 'login':
    return HttpResponse('IG all good, should be battle or location')
  elif state == 'register':
    return HttpResponse('Page after registering?  Maybe location')
# Instagram sends a token here
# Make sure token matches current user or is new
def redirect(request):
  state = request.GET.get("state")
  code = request.GET.get("code")
  RedirectURI = 'http://'+request.get_host()+reverse('Instagram:redirect')
  keys = {'client_id':settings.IG_CLIENT_ID,'client_secret':settings.IG_CLIENT_SECRET,'grant_type':'authorization_code','redirect_uri':RedirectURI,'code':code }
  p = requests.post('https://api.instagram.com/oauth/access_token',data=keys)
  candidate_token = p.json()['access_token']
  stored_token = request.user.userprofile.ig_token
  token_not_exist = UserProfile.objects.filter(ig_token = candidate_token).count() == 0
  if candidate_token == stored_token: #proceed 
    updateIGdata(request.user.userprofile,p.json()['user'])
    return HttpResponse(request.user.userprofile)
    #return getRedirectURL(state)
  elif token_not_exist: #update db
    request.user.userprofile.ig_token = candidate_token
    request.user.userprofile.save()
    updateIGdata(request.user.userprofile,p.json()['user'])
    return HttpResponse(request.user.userprofile) 
    #return getRedirectURL(state)
  else: # token exists for some other account - > logout
    HttpResponseRedirect('https://instagram.com/accounts/logout/')
    
# Get Profilepic from Instagram API

