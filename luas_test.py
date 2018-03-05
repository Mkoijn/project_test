from urllib.request import Request, urlopen
from json import loads
from helpers.luas_list import luas_list
import helpers.coordinates as co
from flask import Flask, render_template

my_address = 'Dorset Street Dublin'
my_location = co.my_location(my_address)
closest_stop = co.closest(luas_list(), my_location)
print(closest_stop)

url = 'http://127.0.0.1:5000/stop?id=' + str(closest_stop['number'])

req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows\
                   NT 5.1; de; rv: 1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
              )
data = loads(urlopen(req).read().decode("utf-8"))
print(data)

# Quick Flask Web App
app = Flask(__name__)


class Station:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


nearest_station = Station(data[0]['name'],
                          data[0]['lat'],
                          data[0]['lng']
                          )


@app.route("/luas")
def index():
    return render_template('luas.html', station=nearest_station)


app.run(debug=True, port=5002, use_reloader=False)
