import requests
from django.shortcuts import render
from .models import City

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	city = 'Las Vegas'
	
	cities = City.objects.all()
	
	weather_data = []
	for city in cities :
		
		r=requests.get(url.format(city)).json()
		
		city_weather = {
	   		'city' : city,
	   		'temperature' : r['main']['temp'],
	   		'description' : r['weather'][0]['description'],
           		'icon' : r['weather'][0]['icon']
		}
		
		
    	context = {'city_weather' : city_weather}
	return render(request, 'weather/weather.html' context)
