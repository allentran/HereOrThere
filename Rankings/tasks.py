from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from Rankings.models import Bar,PublicLadder

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
    FSURL = 'https://api.foursquare.com/v2/venues/search?ll='+str(lat)+','+str(lng)+'&'+urllib.urlencode(urldict)
    r = requests.get(FSURL).json()
    if r['meta']['code'] == 200:
        if r['response']['venues']:
            FSDF = pd.DataFrame(r['response']['venues'])
            URLS = ['https://api.instagram.com/v1/locations/search?foursquare_v2_id=' + FSvenueid + '&v=20140226&client_id='+settings.IG_CLIENT_ID+'&client_secret='+settings.IG_CLIENT_SECRET for FSvenueid in FSDF.id]
            rs = (grequests.get(u) for u in URLS)
            Responses = grequests.map(rs)
            FSDF['IGvenueid'] = [GetIGid(response) for response in Responses]
            FSDF['tips'] = [FSstat['tipCount'] for FSstat in FSDF.stats]
            FSDF['checkins'] = [FSstat['checkinsCount'] for FSstat in FSDF.stats]
            FSDF['users'] = [FSstat['usersCount'] for FSstat in FSDF.stats]
            return FSDF.loc[FSDF['IGvenueid']!='Not found', ['name','id','IGvenueid','tips','checkins','users']]
        else:
            return None
    else:
        return None


# score a venue 
def scoreLocation_IG(IGvenueid):
    
    API_URL = 'https://api.instagram.com/v1/locations/'+IGvenueid+'/media/recent?access_token='+'190218586.1fb234f.5eec5203634849ee935cad418d02c99c'
    Likes = []

    while True:
        r = requests.get(API_URL).json()
        import ipdb
        ipdb.set_trace()
        if r['meta']['code'] == 200:
            for img_data in r['data']:
                Likes.append(img_data['likes']['count'])
        if r['pagination']:
            API_URL = r['pagination']['next_url']
        else:
            return np.mean(Likes),len(Likes)


# gets a .02 degree square around a origin lat,lon point 
def scatterGPS(lat,lng):
    delta = 0.02 
    delta_list = np.array([+delta]*2+[-delta]*2)
    lats = lat + np.append(delta_list,0)
    lngs = lng + np.append(np.roll(delta_list,1),0)
    return np.vstack((lats,lngs)).T

def getAllLocations(scatteredLLs):
    Bars = []
    for row in scatteredLLs:
        ListOBars = getLocations(row[0],row[1])
        if ListOBars is not None:
            Bars.append(ListOBars)
    return pd.concat(Bars,ignore_index=True).groupby('IGvenueid').first().reset_index()


# do +/- .02 on lat/lon to get <=200, save in db

# Silverlake 34.0944,-118.2675




    

    

    
    
#   return URLS
#   return FSDF.loc[FSDF['IGvenueid']!='Not found', ['name','id','IGvenueid','tips','checkins','users']]

