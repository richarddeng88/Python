from googlemaps import Client

c = Client(key="AIzaSyDTV6vS1GeEk_pR5ocM_ClRgOSBc1my4oo")

d = c.directions((40.7529737,-73.9925333),(40.7498048,-74.0148914))

steps = c.directions("texarkana","atlanta")[0]["legs"][0]["steps"]

for d in steps:
    print(d['html_instructions'])



#a = geocode(Client(key="AIzaSyDTV6vS1GeEk_pR5ocM_ClRgOSBc1my4oo"),
#        "4135 Elbertson St, Elmhurst, NY,11373")

a = distance_matrix(Client(key="AIzaSyDTV6vS1GeEk_pR5ocM_ClRgOSBc1my4oo"),
                    (40.7529737,-73.9925333),(40.7498048,-74.0148914))
