from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


from Rankings.models import Bar,PublicLadder

from math import radians,cos,sin
from random import uniform
import time
import requests
import grequests 
import urllib
import pandas as pd
import numpy as np

last_week = np.floor(time.time() - 60*60*24*7)

# Get updated categories

FSCatURL = 'https://api.foursquare.com/v2/venues/categories?v=20140226&client_id='+settings.FS_CLIENT_ID+'&client_secret='+settings.FS_CLIENT_SECRET
Cats = requests.get(FSCatURL)
CatsDF = pd.DataFrame(Cats.json()['response']['categories'])

catid = CatsDF.loc[CatsDF['shortName'] == 'Nightlife',:].id     

# returns dataframe of bars, rate limit left else None
def getFSBars(lat,lng):
    urldict = {'client_id':settings.FS_CLIENT_ID,'client_secret':settings.FS_CLIENT_SECRET,'intent':'browse','radius':1000,'limit':50,'categoryId':catid.values[0],'v':20140226}
    FSURL = 'https://api.foursquare.com/v2/venues/search?ll='+str(lat)+','+str(lng)+'&'+urllib.urlencode(urldict)
    try:
        raw_req = requests.get(FSURL)
        r = raw_req.json()
        if r['meta']['code'] == 200:
            if r['response']['venues']:

                FSDF = pd.DataFrame(r['response']['venues'])
            
                FSDF['tips'] = [FSstat['tipCount'] for FSstat in FSDF.stats]
                FSDF['checkins'] = [FSstat['checkinsCount'] for FSstat in FSDF.stats]
                FSDF['users'] = [FSstat['usersCount'] for FSstat in FSDF.stats]
                lats,lngs,distances = [],[],[]

                for ii,bar in FSDF.iterrows():
                    lats.append(bar.location['lat'])
                    lngs.append(bar.location['lng'])
                    distances.append(bar.location['distance'])
                FSDF['lat'] = lats
                FSDF['lng'] = lngs
                FSDF['distance'] = distances
                return FSDF[['name','id','tips','checkins','users','lat','lng','distance']],raw_req.headers['x-ratelimit-remaining']
            else:
                return None,'unknown'
        else:
            return None,'unknown'
    except requests.exceptions.ConnectionError as e:
        print e
        return None,'unknown'



# score a venue 
def scoreLocation_IG(IGvenueid):
    
    API_URL = 'https://api.instagram.com/v1/locations/'+IGvenueid+'/media/recent?access_token='+'190218586.1fb234f.5eec5203634849ee935cad418d02c99c'
    Likes = []

    while True:
        r = requests.get(API_URL).json()
        if r['meta']['code'] == 200:
            for img_data in r['data']:
                Likes.append(img_data['likes']['count'])
        if r['pagination']:
            API_URL = r['pagination']['next_url']
        else:
            return np.mean(Likes),len(Likes)


# gets a random 4 point (random radius) circle of points around a origin lat,lon point 

def scatterGPS(lat,lng):
    radius = uniform(0.01,0.035);
    angles = uniform(0,90)+90*np.array([0,1,2,3])
    lats = radius*np.sin(np.radians(angles))
    lngs = radius*np.cos(np.radians(angles))
    return zip(lats,lngs)
# returns df, remaining FS queries
def getAllLocations(scatteredLLs):
    Bars = []
    for latlons in scatteredLLs:
        ListOBars,FS_queries_left = getFSBars(latlons[0],latlons[1])
        if ListOBars is not None:
            Bars.append(ListOBars)
    Bars = [barlist for barlist in Bars if barlist is not None]
    if Bars: #i.e if you actually found some bars
        return pd.concat(Bars,ignore_index=True).groupby('id').first().reset_index(),FS_queries_left
    else:
        return None,'unknown'



# do +/- .02 on lat/lon to get <=200, save in db

# Silverlake 34.0944,-118.2675



    

    

    
    
#   return URLS
#   return FSDF.loc[FSDF['IGvenueid']!='Not found', ['name','id','IGvenueid','tips','checkins','users']]

