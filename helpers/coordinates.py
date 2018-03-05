from math import cos, asin, sqrt
from geopy.geocoders import Nominatim


def my_location(address):
    '''
    Takes address, returns latitude and longitude
    '''
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print('My current location: ' + location.address)
    my_lat = location.latitude
    my_lon = location.longitude
    loc = {'lat': my_lat, 'lon': my_lon}
    return loc


def distance(lat1, lon1, lat2, lon2):
    '''
    The haversine formula determines the great-circle
    distance between two points on a sphere given
    their longitudes and latitudes.
    '''
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) \
        * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))


def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'],
                                            v['lon'],
                                            p['lat'],
                                            p['lng']))
