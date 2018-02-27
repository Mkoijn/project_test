import coordinates as co
from urllib.request import Request, urlopen
from json import loads


url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=7453c07d7cf230540911a81515a937d8963cbdfe'

req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows\
                        NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
data = loads(urlopen(req).read().decode("utf-8"))

my_address = 'Kevin Street, Dublin 8'
my_location = co.my_location(my_address)

# get closest station to my address
closest_station = co.closest(data, my_location)
print(closest_station)
