'''Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. 
Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки
файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией
Файл с паролями

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()'''



# Установка пакета  simple-crypt под Windows 10 в PyCharm
# Мне установка пакетов и программ от Microsoft не помогла - модуль simple-crypt не устанавливался в систему.
# 1. Создал проект и виртуальное окружение в PyCharm (в проекте  появилась в папка venv) 
# 2. Открыл настройки интерпретатора - два раза мышкой в правом нижнем углу на названии интерпретатора либо Ctrl+Alt+S
# 3. Установил simple-crypt с опцией --no-deps
# 4. Дополнительно пришлось поставить crypto, pycryptodome (полезли ошибки при запуске  кода)
# 5. Файловым менеджером изменил на верхний регистр папку Crypto в виртуальном  окружении проекта ...\venv\Lib\site-packages\Crypto


import simplecrypt
keys =[]

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open('passwords.txt') as string:
    for line in string:
        data = line.strip()
        keys.append(data)

for key in keys:
    try:
        print(simplecrypt.decrypt(key, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        continue
        
        
 #вариант второй

from simplecrypt import decrypt

passwords_list = []  # создаем пустой список для хранения паролей
with open("passwords.txt") as passwords:
    for password in passwords:
        password = password.rstrip()  # считываем фаил построчно и без табуляции
        passwords_list.append(password)  # добавляем ключь в список

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()  # создаем переменную для хранения зашифрованой информации


def decrypt_inf(passw, txt):  # функция принимает 2 объекта - список ключей и зашифорванный текст
    for p in passw:
        try:  # если ключь подходит - возвращаем расшифрованный текст в нормальном формате
            return decrypt(p, txt).decode("utf-8")
        except:  # если нет - переходим к следующему ключу
            continue


print(decrypt_inf(passwords_list, encrypted))
