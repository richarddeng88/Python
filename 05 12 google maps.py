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


-73.9925333

result = gmaps.directions((40.7529737,-73.9925333),
                                         (40.7498048,-74.0148914),
                                     mode="transit",
                                     departure_time=now)
