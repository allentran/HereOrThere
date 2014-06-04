from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from SiteUsers.models import UserProfile,Friends,Education,Location,School
import requests

# update ig_data for userprofile
def updateIGdata(userprofile):
  try:
    token = userprofile.ig_token
  except:
    token = ''
  IGURL = 'https://api.instagram.com/v1/users/self/?access_token='+token
  IG_response = requests.get(IGURL).json()
  if IG_response['meta']['code'] == 200: #IG not accepted for some reason
    userprofile.ig_username = IG_response['data']['username']
    userprofile.ig_pic = IG_response['data']['profile_picture']
    userprofile.ig_follows = IG_response['data']['follows']
    userprofile.ig_followers = IG_response['data']['followed_by']
    userprofile.save()
    return True
  else:
    return False

# Check if current token is valid by trying to update
def check(request):
  if updateIGdata(request.user.userprofile): 
    return HttpResponse('IG all good, should be battle or location')
  else: #go login and get a new token
    RedirectURI = 'http://'+request.get_host()+reverse('Instagram:redirect')
    IGUrl = 'https://api.instagram.com/oauth/authorize/?client_id='+settings.IG_CLIENT_ID+'&response_type=code'+'&state=login'+'&redirect_uri='+RedirectURI
    return HttpResponseRedirect(IGUrl)

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
  candidate_token = request.GET.get("code")
  stored_token = request.user.userprofile.ig_token
  token_not_exist = UserProfile.objects.filter(ig_token = candidate_token).count() == 0
  if candidate_token == stored_token: #proceed 
    updateIGdata(request.user.userprofile)
    return getRedirectURL(state)
  elif token_not_exist: #update db
    request.user.userprofile.ig_token = candidate_token
    request.user.userprofile.save()
    updateIGdata(request.user.userprofile) 
    return getRedirectURL(state)
  else: # token exists for some other account - > logout
    HttpResponseRedirect('https://instagram.com/accounts/logout/')
    
# Get Profilepic from Instagram API

