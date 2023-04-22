''' к уроку из курса "Python основы и преминения" раздел "немного про интернет"
в данном примере обращаемся к сайту с документацией пайона 3.5 и сохраняем иконку в файл на ПК, также пробуем другие простые операции

requests.get принимает url также можно предать параметры и значения, например:

requests.get('https://yandex.ru/search/', 
              param={'text': 'Stepik'})

'''

import requests

res = requests.get('https://docs.python.org/3.5/_static/py.png')
print(res.status_code)
print(res.headers['Content-Type'])

with open('python.png', 'wb') as f:
    f.write(res.content)

# print(res.content)
#print(res.text)

# for k, v in res.headers.items():
#     print(f'{k}: {v}')


