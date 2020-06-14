import requests
from utils import textReader

class WeatherHandler:
    def __init__(self):
        self.key = 'f9dd155e5974455d16ab8feb3e55e746'

    def getWeather(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Wroclaw,pl&units=metric&appid=' + self.key)
        data = response.json()
        temperature = 'Obecna temperatura w ' + data["name"] + ' wynosi ' + str(data["main"]["temp"]) + 'stopnie celcjusza. '
        wind = 'Prędkość wiatru: ' + str(data["wind"]["speed"]) + ' metra na sekundę. '
        pressure = 'Ciśnienie: ' + str(data["main"]["pressure"]) + ' hektopaskali. '
        textReader(temperature + wind + pressure)
        

