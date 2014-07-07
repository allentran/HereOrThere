# find bars for each neighborhood
# bars are associated with the closest neighborhood
from django.conf import settings

from Rankings.models import Bar,BarLocations
from SiteUsers.models import Neighborhood,City
from Rankings.tasks import scatterGPS,getAllLocations

import datetime

import requests
import grequests 
import pandas as pd
import numpy as np

FSCatURL = 'https://api.foursquare.com/v2/venues/categories?v=20140226&client_id='+settings.FS_CLIENT_ID+'&client_secret='+settings.FS_CLIENT_SECRET
Cats = requests.get(FSCatURL)
CatsDF = pd.DataFrame(Cats.json()['response']['categories'])
catid = CatsDF.loc[CatsDF['shortName'] == 'Nightlife',:].id

def findBars(Hood):
	BarsInHood,FS_queries_left = getAllLocations(scatterGPS(Hood.lat,Hood.lng))
	if BarsInHood is not None:
		for ii,bar in BarsInHood.iterrows():
			try:
				bar_db,bar_created = Bar.objects.get_or_create(FS_id=bar['id'],
					              Name=bar['name'],lat=bar['lat'],lng=bar['lng'])
				barlocation, created = BarLocations.objects.get_or_create(bar=bar_db,neighborhood=Hood,distance=bar['distance'])
				if bar_created:
					print 'Found ' + bar['name'] + ' in ' + Hood.neighborhood_name + ', ' + Hood.city.city_name
			except Exception, e:
				print repr(e)
			
		Hood.bars_last_updated = datetime.datetime.today()
		Hood.save()
	return FS_queries_left

Hoods = Neighborhood.objects.all().order_by('bars_last_updated','city')

# loop over hoods
for ii,hood in enumerate(Hoods):
	FS_left = findBars(hood)
	if FS_left is 'unknown':
		pass
	elif (FS_left < 10) & (FS_left > 0):
		print 'Exhausted FS for today'
		# should write log
		break
	print 'Done with ' + hood.neighborhood_name + ', ' + hood.city.city_name + ' (' + str( np.round(100.0*(ii+1)/len(Hoods),2) ) + '% completed)'

# Bars that require IG_ids

Bars_missing_IG = Bar.objects.all().filter(IG_id='')
for bar in Bars_missing_IG:
	bar.GetIG_ID()



