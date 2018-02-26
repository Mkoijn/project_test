from bs4 import BeautifulSoup
import urllib.request
import coordinates as co

request = urllib.request.urlopen(
    'http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML_WithStationType?StationType=D')

xml = BeautifulSoup(request, 'xml')

my_l = []
for item in xml.findAll('objStation'):
    my_l.append(item.text)
# print(my_l)

new_l = []
for thing in my_l:
    a = thing.split('\n')
    new_l.append(a)
# print(new_l)

l1 = []
for yoke in new_l:
    d1 = {}
    d2 = {}
    d1['station_name'] = yoke[1]
    d2['lat'] = float(yoke[3])
    d2['lng'] = float(yoke[4])
    d1['position'] = d2
    l1.append(d1)
# print(l1)

my_address = "Belfast"

my_location = co.my_location(my_address)
closest_stop = co.closest(l1, my_location)
print(closest_stop)
