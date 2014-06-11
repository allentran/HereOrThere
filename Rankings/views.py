from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

import grequests 
import urllib
import pandas as pd

# return IGid mapping to FSid
def GetIGid(response):
		if len(response.json()['data']) == 0:
			return 'Not found'
		else:
			return response.json()['data'][0]['id']

# get list of instagram_ids
# if user's ig_token is available, use it!
def getLocations(lat,lng):
	urldict = {'client_id':settings.FS_CLIENT_ID,'client_secret':settings.FS_CLIENT_SECRET,'intent':'browse','radius':1000,'limit':50,'categoryId':catid.values[0],'v':20140226}
	FSURL = 'https://api.foursquare.com/v2/venues/search?ll='+lat+','+lng+'&'+urllib.urlencode(urldict)
	FSDF = pd.DataFrame(requests.get(FSURL).json()['response']['venues'])
	
	URLS = ['https://api.instagram.com/v1/locations/search?foursquare_v2_id=' 
	        + FSvenueid + '&v=20140226&client_id='+IG_id+'&client_secret='+IG_sec 
	        for FSvenueid in FSDF.id]
	rs = (grequests.get(u) for u in URLS)
	Responses = grequests.map(rs)
	
	FSDF['IGvenueid'] = [GetIGid(response) for response in Responses]
	FSDF['tips'] = [FSstat['tipCount'] for FSstat in FSDF.stats]
	FSDF['checkins'] = [FSstat['checkinsCount'] for FSstat in FSDF.stats]
	FSDF['users'] = [FSstat['usersCount'] for FSstat in FSDF.stats]
	return FSDF.loc[FSDF['IGvenueid']!='Not found', ['name','id','IGvenueid','tips','checkins','users']]


	

	

	
	
#	return URLS
	return FSDF.loc[FSDF['IGvenueid']!='Not found', ['name','id','IGvenueid','tips','checkins','users']]


def public(request):
# Query DB and get rankings for Los Angeles, New York and Sydney
# For now, show public rankings using average likes of photos of venue
# Photos_dm^0.5 Likes_dm
# silverlake 34.0932287,-118.2674252
	return None

def private(request):
# Get rankings for user location
	return None
