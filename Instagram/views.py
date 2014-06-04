from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from SiteUsers.models import UserProfile,Friends,Education,Location,School

# Create your views here.

def redirect(request):
	request.user.UserProfile
	request.GET.get("code")
