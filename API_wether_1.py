'''
API https://openweathermap.org/ - предоставляет информацию о погоде
'''

import requests

city = input()
api_url = "https://api.openweathermap.org/data/2.5/weather"
params ={
    'q': city,
    'appid': '17ffec53c7660003386c4c304f4fcc93',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
data = res.json()
# for k, v in data.items():
#     print(f'{k}: {v}')

print(f"Current temperature in {city} is {(data['main']['temp'])}")

'''-> Current temperature in Moscow is 11.73'''
