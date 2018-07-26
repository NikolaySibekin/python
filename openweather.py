__author__ = 'Николай Сибекин'

import requests
import sys

# Регистрируемся на OpenWeatherMap.org и получаем APP key
app_id = "6d8e495ca73d5bbc1d6bf8ebd52c4123"

# Проверяем наличие в базе информации о нужном населенном пункте
def get_city_id(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
            params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])]
        for d in data['list']:
            print("город: ", cities)
            city_id = data['list'][0]['id']
            print('city_id=', city_id)
    except Exception as e:
        print("Исключение (поиск нужного населенного пункта): ", e)
        pass
    assert isinstance(city_id, int)
    return city_id

# Запрашиваем текущую погоду
def request_current_weather(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        print("погодные условия: ", data['weather'][0]['description'])
        print("температура: ", data['main']['temp'])
        print("температура (минимальная): ", data['main']['temp_min'])
        print("температура (максимальная): ", data['main']['temp_max'])
        print("дата: ", data)
    except Exception as e:
        print("Исключение (текущая погода): ", e)
        pass

# Запрашиваем прогноз погоды на 5 дней
def request_forecast(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        for i in data['list']:
            print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                get_wind_direction(i['wind']['deg']),
                i['weather'][0]['description'] )
    except Exception as e:
        print("Исключение (прогноз погоды): ", e)
        pass

#city_id для Санкт-Петербурга
city_id = 519690

if len(sys.argv) == 2:
    s_city_name = sys.argv[1]
    print("город:", s_city_name)
    city_id = get_city_id(s_city_name)
elif len(sys.argv) > 2:
    print('Санкт-Петербург,РФ')
    sys.exit()

print("\nТекущая погода")
request_current_weather(city_id)

print("\nПрогноз на 5 дней")                  
request_forecast(city_id)
