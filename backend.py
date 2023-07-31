from geopy.geocoders import Nominatim
import requests

API_KEY = 'ffcb1f5887f077aeeafec40d4d4925ce'


def data(place, days):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(place)
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    filter_data = filter_data[:8*days]
    return filter_data

