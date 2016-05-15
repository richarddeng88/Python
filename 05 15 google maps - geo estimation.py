import pandas as pd
import googlemaps
from datetime import datetime
import numpy

gmaps = googlemaps.Client(key='AIzaSyDTV6vS1GeEk_pR5ocM_ClRgOSBc1my4oo')

df = pd.read_csv('estimation.csv')

# Request directions via public transit
now = datetime.now()
## find the optimized steps, time consumed, and distance
info = gmaps.directions((40.7529737,-73.9925333),(40.7498048,-74.0148914),
                        mode='bicycling',
                        departure_time=now)[0]["legs"][0]
                    # this function 'legs' only include steps, duration, distance three factors. 

##### estimating the distance and duration time for SPEED COMPARISION#############
##main_df = pd.DataFrame(columns=('duration','distance'))
##dur = list()
##dis = list()
##
##for a in df['index']:
##        print('ready to work on ', a)
##        st_lati = df['start.station.latitude'][df['index']==a]
##        st_long = df['start.station.longitude'][df['index']==a]
##        end_lati = df['end.station.latitude'][df['index']==a]
##        end_long = df['end.station.longitude'][df['index']==a]
##        info = gmaps.directions((float(st_lati),float(st_long)),(float(end_lati),float(end_long)),
##                        mode='bicycling',
##                        departure_time=now)[0]["legs"][0]
##        print('the distance info of ', a, 'has been written')
##        duration = info["duration"]['value']
##        #print('the time used is ', duration)
##        distance = info['distance']['value']
##        #print('the distance is ', distance)
##        dur.append(duration)
##        dis.append(distance)
##        s = pd.Series([duration,distance],index=['duration','distance'])
##        main_df = main_df.append(s,ignore_index=True)
##
##main_df.to_csv('citi/dis_estimation.csv')


###### estimationg one day data for CARTODB animated geographing###################

main_df = pd.DataFrame(columns=('index','latitude','longitude','duration'))
dur = list()
dis = list()

for a in df['index']:
        print('ready to work on ', a)
        st_lati = df['start.station.latitude'][df['index']==a]
        st_long = df['start.station.longitude'][df['index']==a]
        end_lati = df['end.station.latitude'][df['index']==a]
        end_long = df['end.station.longitude'][df['index']==a]
        info = gmaps.directions((float(st_lati),float(st_long)),(float(end_lati),float(end_long)),
                        mode='bicycling',
                        departure_time=now)[0]["legs"][0]
        print('the distance info of ', a, 'has been written')
        
        steps = info["steps"]
        for d in steps:
                #print(d['end_location'],d['duration']['value'])
                lat = d['end_location']['lat']
                lng = d['end_location']['lng']
                dur = d['duration']['value']
                s = pd.Series([a,lat,lng,dur],index=['index','latitude','longitude','duration'])
                main_df = main_df.append(s,ignore_index=True)

main_df.to_csv('citi/geo_estimation.csv')





































    
