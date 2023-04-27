'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
'''


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
result = {}
with open('dataset_24476_4.txt', encoding='utf-8') as data:
    for line in data:
        id_art = line.strip()
        url_api = f"https://api.artsy.net/api/artists/{id_art}"
        req = requests.get(url_api, headers=headers).json()
        result[req['birthday']] = req['sortable_name']
        
for k,v in sorted(result.items()):
    print(f'{v}')
