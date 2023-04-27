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
    
    
#вариант два(с классом)

import requests

client_id = "..."
client_secret = "..."
path = "dataset_24476_4.txt"


class Artist:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Artists:
    def __init__(self, ids, token):
        self.ids = ids
        self.artists = []
        self.token = token

    def _get_name_and_year(self):
        header = {"X-Xapp-Token": self.token}
        for artist_id in self.ids:
            artist_id = artist_id.strip()
            url = f"https://api.artsy.net/api/artists/{artist_id}"
            res = requests.get(url, headers=header)
            res = res.json()
            name, year = res["sortable_name"], res["birthday"]
            self.artists += [Artist(name, year)]

    def sort_artists_by_birthday(self):
        self._get_name_and_year()
        self.artists.sort(key=lambda artist: artist.year)
        for artist in self.artists:
            print(artist.name)


def get_token(id, secret):
    data = {
        "client_id": id,
        "client_secret": secret
    }
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token", data)
    j = r.json()
    return j["token"]


def get_artist_ids(path):
    with open(path) as f:
        artist_ids = f.readlines()
        return artist_ids


token = get_token(client_id, client_secret)
ids = get_artist_ids(path)
artists = Artists(ids, token)
artists.sort_artists_by_birthday()


# вариант три

import requests
import json


class Artist:
    """
    Класс, хранящий в себе имя и год рождения художника
    """
    def __init__(self, artist_name, artist_birthday):
        self.artist_name = artist_name
        self.artist_birthday = artist_birthday

    def __repr__(self):
        return f"{self.artist_name} : {self.artist_birthday}"


client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)  # достаем токен
token = j["token"]  # создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token} # инициируем запрос с заголовком
artist_list = []
with open("dataset_24476_4.txt", "r") as data:
    for artist_id in data:
        artist_id = artist_id.strip()
        r = requests.get(f"https://api.artsy.net/api/artists/{artist_id}", headers=headers)
        r.encoding = 'utf-8'  # декодируем 
        j = r.json()  # разбираем ответ сервера
        name = j['sortable_name']
        birthday = int(j['birthday'])
        artist_list.append(Artist(name, birthday))  # добавляем объект класса в список


artist_sorted = sorted(artist_list, key=lambda a: (a.artist_birthday, a.artist_name))
# сортируем список по году рождения, если год рождения одинаковый - по имени
for artist in artist_sorted:
    print(artist.artist_name)
