from django.shortcuts import render

	def index(request):
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
		city = 'Las Vegas'
		
		r=requests.get(url.format(city))
    		print(r.text)
		return render(request, 'weather/weather.html')
