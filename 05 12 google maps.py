import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDTV6vS1GeEk_pR5ocM_ClRgOSBc1my4oo')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
result = gmaps.directions("Sydney Town Hall",
                                          "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


result = gmaps.directions((40.7529737,-73.9925333),
                                         (40.7498048,-74.0148914),
                                     mode="transit",
                                     departure_time=now)

## find the optimized steps and time consumed
steps = gmaps.directions((40.7529737,-73.9925333),(40.7498048,-74.0148914))[0]["legs"][0]["steps"]
duration = gmaps.directions((40.7529737,-73.9925333),
                            (40.7498048,-74.0148914))[0]["legs"][0]["duration"]['value']
for d in steps:
    print(d['html_instructions'])
for d in steps:
    print(d['end_location'])
a = "time consumed is "+ str(duration) +" seconds"
print(a)
## calcuate the optimized geo distance 
distance = gmaps.distance_matrix((41.7529737,-73.9925333),(40.7498048,-74.0148914))
print(distance['status'])
print(distance['rows'])
print(distance['origin_addresses'])
print(distance['destination_addresses'])
dist=distance['rows'][0]['elements'][0]['distance']['value']
b = "the distance is " + str(dist) + " meters"
print b








