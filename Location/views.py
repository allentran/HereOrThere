from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from SiteUsers.models import UserProfile
from django.contrib.auth.models import User

@login_required
def index(request):
	if request.session['IG_authd']:
		context={'goog_key':settings.GOOG_KEY}
		return render(request,'Location/locateme.html',context)
	else:
		return HttpResponseRedirect(reverse('SiteUsers:instagram')+'?state='+'login')

def instructions(request):
	if request.session['IG_authd']:
		return render(request,'Location/instructions.html',context)
	else:
		return HttpResponseRedirect(reverse('SiteUsers:instagram')+'?state='+'login')

