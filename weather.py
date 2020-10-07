import requests


# API = 'c786c37d50173994fca6ad4a31029e5d'

# def local_request():
#     r = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx', params={
#     'q': 'Grozny',
#     'key': 'ffb4c5cabce246789e5190516202009',
#     'format': 'json', 
#     'num_of_days': 1,
#     'lang': 'ru'
#     })
#     return r.json()



# weather = local_request()

# print(weather['data']['weather'][0]['mintempC'])\




def local_request(citys):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
    'q': citys,
    'appid': 'c786c37d50173994fca6ad4a31029e5d',
    'mode': 'json', 
    'lang': 'ru',
    'units': 'metric'
    })
    return r.json()

print(local_request('Грозный'))

# if __name__ == '__main__':
#     f = local_request()

# citys = input('Город: ')

# weather = local_request(citys)
# print(weather['name'])
# print(str(weather['main']['temp']) + '°')







# def local_request():
#     r = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly', params={
#     'q': 'London',
#     'appid': '2cdfffe6a3ab2b2451d820682ab3d8f4',
#     'mode': 'json', 
#     'lang': 'ru',
#     'cnt': 3
#     })
#     return r.json()


# weather = local_request()
# # print(weather['name'])
# # print(weather['main']['temp'])
# print(weather)