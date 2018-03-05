import helpers.coordinates as co
from urllib.request import Request, urlopen
from json import loads
from flask import Flask, render_template

url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=7453c07d7cf230540911a81515a937d8963cbdfe'

req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows\
                        NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
data = loads(urlopen(req).read().decode("utf-8"))

my_address = '19 Ebenezer Terrace'
my_location = co.my_location(my_address)
print(my_location)

for item in data:
    item['lat'] = item['position']['lat']
    item['lng'] = item['position']['lng']
    item.pop('position', None)
closest_station = co.closest(data, my_location)
print('CLOSEST STATION:')
print(closest_station)


# Quick Flask Web App
app = Flask(__name__)


class Station:
    def __init__(self, key, name, lat, lng, stands, bikes, status):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng
        self.stands = stands
        self.bikes = bikes
        self.status = status


nearest_station = Station(closest_station['number'],
                          closest_station['name'],
                          closest_station['lat'],
                          closest_station['lng'],
                          closest_station['available_bike_stands'],
                          closest_station['available_bikes'],
                          closest_station['status'])


@app.route("/bikes")
def index():
    return render_template('bikes.html', station=nearest_station)


app.run(debug=True, port=5001, use_reloader=False)
