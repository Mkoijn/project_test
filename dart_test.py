from bs4 import BeautifulSoup
import urllib.request
import helpers.coordinates as co

request = urllib.request.urlopen(
    'http://api.irishrail.ie/realtime/realtime.asmx/getAllStations'
    'XML_WithStationType?StationType=D')

xml = BeautifulSoup(request, 'xml')

my_xml_stations = []
for item in xml.findAll('objStation'):
    my_xml_stations.append(item.text)
# print(my_l)

stations = []
for thing in my_xml_stations:
    a = thing.split('\n')
    stations.append(a)
# print(new_l)

list_dict_stations = []
for yoke in stations:
    d1 = {}
    d1['station_name'] = yoke[1]
    d1['lat'] = float(yoke[3])
    d1['lng'] = float(yoke[4])
    list_dict_stations.append(d1)
# print(list_dict_stations)

my_address = "Belfast"

my_location = co.my_location(my_address)
closest_stop = co.closest(list_dict_stations, my_location)
print(closest_stop)
