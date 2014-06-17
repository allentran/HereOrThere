from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

@login_required
def index(request):
	ll = request.GET.get('lat') + ',' + request.GET.get('lon')
	return HttpResponse(str(ll))
