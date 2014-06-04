from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from SiteUsers.models import UserProfile,Friends,Education,Location,School


# Check if token is valid
def check(request):

# Instagram sends a token here
# Make sure token matches current user or is new
def redirect(request):
  candidate_token = request.GET.get("code")
  stored_token = request.user.userprofile.ig_token
  token_not_exist = UserProfile.objects.filter(ig_token = candidate_token).count() == 0
  if candidate_token == stored_token: 
    return HttpResponseRedirect()
  elif token_not_exist:
    request.user.userprofile.ig_token = candidate_token
    request.user.userprofile.save()
    return HttpResponseRedirect()
  else: # get your own ig
    HttpResponseRedirect('https://instagram.com/accounts/logout/')
    
# Get Profilepic from Instagram API

