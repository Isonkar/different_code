import requests
import json

# генерируем токен и сохраняем в переменную токен 
client_id = '......................' # данные берем https://developers.artsy.net/v2/start?id=644a1467583b4c000bb3f6a8
client_secret = '......................' # данные берем https://developers.artsy.net/v2/start?id=644a1467583b4c000bb3f6a8

r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                 data={
                   'client_id': client_id,
                   'client_secret': client_secret
                 })
j = json.loads(r.text)
token = j['token']  

