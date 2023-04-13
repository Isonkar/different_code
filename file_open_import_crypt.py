'''Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. 
Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с
интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией
Файл с паролями

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()'''

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
    except: continue
      
      
          
# вариант второй

import simplecrypt

encrypted = open("encrypted.bin", "rb").read()
passwords = open("passwords.txt").readlines()

for p in passwords:
    p = p.strip()
    try:
        s = simplecrypt.decrypt(p, encrypted)
    except simplecrypt.DecryptionException:
        continue

    print(s.decode("utf-8"))
 
#вариант три

import urllib
from simplecrypt import decrypt

ciphertext = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/encrypted.bin').read()
passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

for password in passwords:
    try:
        plaintext = decrypt(password.strip(), ciphertext)
    except:
        pass
    else:
        print(plaintext)
