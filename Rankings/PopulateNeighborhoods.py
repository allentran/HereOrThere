import pandas as pd
import numpy as np
import requests
from django.conf import settings
from SiteUsers.models import City, Neighborhood

def geocodeHood(loc_str):
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+loc_str+'&key='+settings.GOOG_KEY)
	if r.json()['status'] == 'OK':
		loc_data = r.json()['results'][0]['geometry']['location']
		lat = loc_data['lat']
		lng = loc_data['lng']
		return lat,lng
	else: 
		return None

HoodsDF = pd.read_csv('Neighborhoods.csv')

# geocode neighborhoods missing lat/lng

for ii,hood in HoodsDF.iterrows():
	if (hood['lat'] > -1000) & (hood['lng'] > -1000):
		pass
	else: # lat missing
		HoodsDF.loc[ii,'lat'],HoodsDF.loc[ii,'lng'] = geocodeHood(hood.Neighborhood+', '+hood.City+', '+hood.State)
	print ii

# Add Hoods, will by default also add cities if need be

hoods = HoodsDF.groupby('Neighborhood').first().reset_index()

# get earliest bars_last_updated

earliest_date = Neighborhood.objects.all().order_by('bars_last_updated')[0].bars_last_updated


for ii,city_hood in hoods.iterrows():
	db_city, created = City.objects.get_or_create(city_name=city_hood['City'],state=city_hood['State'])
	db_neighborhood, created = Neighborhood.objects.get_or_create(neighborhood_name=city_hood['Neighborhood'],
		                        city=db_city,bars_last_updated=earliest_date)
	db_neighborhood.lat = city_hood['lat']
	db_neighborhood.lng = city_hood['lng']
	db_neighborhood.save()


HoodsDF.to_csv('Neighborhoods.csv',index=False)



