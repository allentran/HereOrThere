from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse

def test(request):
	RedirectURI = 'http://'+request.get_host()+reverse('IGsuccess')
	IGUrl = 'https://api.instagram.com/oauth/authorize/?client_id='+settings.IG_CLIENT_ID+'&redirect_uri='+RedirectURI+'&response_type=code'
	context = {"FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID,'FBPermissions': settings.FACEBOOK_PERMISSIONS}
	return render(request,"FBLogin/fblogin_test.html", context)

def index(request):
	context = {"FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID,'FBPermissions': settings.FACEBOOK_PERMISSIONS}
	return render(request,"FBLogin/fblogin.html", context)

def FB_success(request):

	request.session['access_token'] = request.GET.get("access_token")
	
	RedirectURI = 'http://'+request.get_host()+reverse('IGsuccess')
	IGUrl = 'https://api.instagram.com/oauth/authorize/?client_id='+settings.IG_CLIENT_ID+'&redirect_uri='+RedirectURI+'&response_type=code'

# Should update FB database

  #  r = requests.get('https://graph.facebook.com/v2.0/me?access_token='+request.session['access_token']).json()
    
# Get location and send to IG Login
	return HttpResponseRedirect(IGUrl)
    
def IG_success(request):

    request.session['IGtoken'] = request.GET.get("code")
    request.session['authd'] = True
    # Get location and send to location
    RedirectURI = 'http://'+request.get_host()+reverse('LocationView')
    return HttpResponseRedirect(RedirectURI)

