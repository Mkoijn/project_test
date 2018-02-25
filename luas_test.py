import luas.api
from luas.api import LuasDirection
from geopy.geocoders import Nominatim
import coordinates as co

geolocator = Nominatim()
location = geolocator.geocode("19 Ebenezer Terrace")
print(location.address)
my_lat = location.latitude
my_lon = location.longitude
print(my_lat, my_lon)

stops = [{'stop_name': 'FOU', 'lat': 53.346421, 'lon': -6.273455},
         {'stop_name': 'FAT', 'lat': 53.338248, 'lon': -6.294419},
         {'stop_name': 'RED', 'lat': 53.318460, 'lon': -6.373240}]


loc = {'lat': my_lat, 'lon': my_lon}
closest_stop = co.closest(stops, loc)
print(closest_stop)


lc = luas.api.LuasClient()
print(lc.next_tram(closest_stop['stop_name'], LuasDirection.Inbound).due)
print(lc.next_tram(closest_stop['stop_name'], LuasDirection.Outbound).due)
