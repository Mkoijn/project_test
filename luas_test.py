import luas.api
from luas.api import LuasDirection
from math import cos, asin, sqrt
from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator.geocode("Kevin St Dublin 2")
print(location.address)
my_lat = location.latitude
my_lon = location.longitude
print(my_lat, my_lon)

locs = [{'stop_name': 'FOU', 'lat': 53.346421, 'lon': -6.273455},
        {'stop_name': 'FAT', 'lat': 53.338248, 'lon': -6.294419},
        {'stop_name': 'RED', 'lat': 53.318460, 'lon': -6.373240}]


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) \
        * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))


def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'],
                                            v['lon'], p['lat'], p['lon']))


v = {'lat': my_lat, 'lon': my_lon}
closest_stop = closest(locs, v)
print(closest_stop)


lc = luas.api.LuasClient()
print(lc.next_tram(closest_stop['stop_name'], LuasDirection.Inbound).due)
print(lc.next_tram(closest_stop['stop_name'], LuasDirection.Outbound).due)
