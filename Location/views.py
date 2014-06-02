from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from SiteUsers.models import UserProfile
from django.contrib.auth.models import User
@login_required
def index(request):
	# verify instagram token is valid
	request.user.userprofile
	BattleURL = 'http://'+request.get_host()+reverse('InitBattleView')
	context = {"BattleURL": BattleURL}
	return HttpResponse(request.user)