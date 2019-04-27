from django.shortcuts import render

	def index(request):
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
		city = 'Las Vegas'
		
		r=requests.get(url.format(city))
		
		city_weather = {
	   	'city' : city,
		'temperature' : r['main']['temp'],
		'description' : r['weather'][0]['description'],
		'icon' : r['weather'][0]['icon']
		}
		
		
    		context = {'city_weather' : city_weather}
		return render(request, 'weather/weather.html' context)
