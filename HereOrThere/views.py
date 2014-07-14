from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def home(request):
	if 'next' in request.GET:
		next_url = request.GET['next']
	if not request.user.is_authenticated():
		# context = {'next_url':next_url}
		context = {}
		return render(request,'base_login.html',context)
	else:
		return HttpResponse('Hi')		
