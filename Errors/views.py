from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from SiteUsers.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


def index(request):
  error_code = request.GET['errorcode']
  if error_code == 'IGserver':
    error_msg = 'Error: Instagram server'
  elif error_code == 'FBserver':
    error_msg = 'Error: Facebook server'
  else:
    error_msg = 'Error: unspecified'
  context = {'error_msg':error_msg}  
  return render(request,'Errors/error.html',context)