from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


def public(request):
# Query DB and get rankings for Los Angeles, New York and Sydney
	return None

def private(request):
# Get rankings for user location
	return None
