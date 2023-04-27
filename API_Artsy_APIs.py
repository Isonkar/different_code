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

# формирвоание запроса/ получение данных
headers = {'X-Xapp-Token' : token}

with open('dataset_24476_4.txt', encoding='utf-8') as data:
    for line in data:
        id_art = line.strip()
        url_api = f"https://api.artsy.net/api/artists/{id_art}"
        req = requests.get(url_api, headers=headers).json()
        print(f"{req['sortable_name']}: {req['birthday']}")
