import requests
import json

url = 'https://overpass-api.de/api/interpreter'

query = '''
[out:json];
area["ISO3166-1"="RU"][admin_level=2];
(
  rel[boundary=administrative][admin_level=4](area);
  >;
);
out body;
'''

response = requests.get(url, params={'data': query})
data = response.json()
with open('data.json', 'w') as file:
    file.write(json.dumps(data))

# for element in data['elements']:
#     if element['type'] == 'relation':
#         name = None
#         coordinates = []
#         for tag in element['tags']:
#             if tag['k'] == 'name:en':
#                 name = tag['v']
#             elif tag['k'] == 'boundary':
#                 boundary = tag['v']
#         for member in element['members']:
#             if member['type'] == 'way':
#                 way_id = member['ref']
#                 way = next((e for e in data['elements'] if e['type'] == 'way' and e['id'] == way_id), None)
#                 if way:
#                     for coordinate in way['geometry']:
#                         coordinates.append([coordinate['lat'], coordinate['lon']])
#         if name and coordinates:
#             print(f"{name}: {boundary}, {coordinates}")
