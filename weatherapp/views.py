from django.shortcuts import render
import requests
from .models import Cities
from .forms import CityForm

# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=679f33bdead47dee2bdf2ad03c8c008b'
    # city='Chandigarh'

    if request.method=='POST':
        # form =CityForm(request.POST)
        # form.save()
        pass

    # form=CityForm()

    cities = Cities.objects.all()

    weather_data=[]

    for city in cities:

        r=requests.get(url.format(city)).json()
        # print(r.text)

        city_weather={
            'city':city.city,
            'desc':r['weather'][0]['description'],
            'temp':r['main']['temp'],
            'mintemp':r['main']['temp_min'],
            'maxtemp':r['main']['temp_max'],
            'pressure':r['main']['pressure'],
            'humidity':r['main']['humidity'],
            'windspeed':r['wind']['speed'],
            'icon':r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
        weather_data.reverse()

    print(weather_data)

    context={
        'weather_data':weather_data, 
        'city_weather':city_weather, 
        # 'form':form
    }

    return render(request,'weather/weather.html', context)
