from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
	ll = request.GET.get('lat') + ',' + request.GET.get('lon')
	return HttpResponse(str(ll))
