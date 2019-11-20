import reverse_geocoder as rg 
import pandas as pd
import numpy as np 
import pprint
flag = ''
data  = {'Site 1': '35.028309, 135.753082',
                'Site 2': '46.469391, 30.740883',
                'Site 3': '39.758949, -84.191605',
                'Site 4': '41.015137, 28.979530',
                'Site 5': '24.466667, 54.366669',
                'Site 6': '3.140853, 101.693207',
                #_
                'Site 7': '9.005401, 38.763611',
                'Site 8': '-3.989038, -79.203560',
                'Site 9': '52.377956, 4.897070',
                'Site 10': '41.085651, -73.858467',
                'Site 11': '57.790001, -152.407227',
                'Site 12': '31.205753, 29.924526'}

df = pd.DataFrame.from_dict(data, orient='index')
lat = []
lon = []
for row in df[0]:
    try:
        lat.append(float(row.split(', ')[0]))
        lon.append(float(row.split(',')[1]))
    except:
        lat.append(np.NaN)
        lon.append(np.NaN)
df['latitude'] = lat
df['longitude'] = lon 

for i in range(len(data)):
    coordinates = (df['latitude'][i], df['longitude'][i])

    results = rg.search(coordinates)
    firstLet = results[0]['name']
    flag += firstLet[0]
flag = 'picoCTF{' + str(flag) + '}'
print(flag)
