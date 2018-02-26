import luas.api
from luas.api import LuasDirection
import coordinates as co

stops = [{'stop_name': 'FOU', 'position': {'lat': 53.346421,
                                           'lng': -6.273455}},
         {'stop_name': 'FAT', 'position': {'lat': 53.338248,
                                           'lng': -6.294419}},
         {'stop_name': 'RED', 'position': {'lat': 53.318460,
                                           'lng': -6.373240}}]

my_address = 'Kevin Street, Dublin 8'

my_location = co.my_location(my_address)
closest_stop = co.closest(stops, my_location)
print(closest_stop)

lc = luas.api.LuasClient()
print('Inbound due: ' + str(lc.next_tram(closest_stop['stop_name'],
                                         LuasDirection.Inbound).due))
print('Outbound due: ' + str(lc.next_tram(closest_stop['stop_name'],
                                          LuasDirection.Outbound).due))
