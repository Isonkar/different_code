'''
https://rapidapi.com/
перевод фразы, данный API сервис можно использовать в своих проектах
'''


import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
	"q": str(input('Введите фразу для перевода(на английском языке): ')),
	"target": "ru",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "INTER YOUR KEY",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)



print(response.json()['data']['translations'][0]['translatedText'])

#{'data': {'translations': [{'translatedText': 'здесь будет результат перевода'}]}}
