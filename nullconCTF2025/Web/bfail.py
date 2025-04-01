import requests
import urllib.parse

url = "http://52.59.124.14:5013/"
username = b'admin'
password = b'\xec\x9f\xe0a\x978\xfc\xb6:T\xe2\xa0\xc9<\x9e\x1a\xa5\xfao\xb2\x15\x86\xe5$\x86Z\x1a\xd4\xca#\x15\xd2x\xa0\x0e0\xca\xbc\x89T\xc5V6\xf1\xa4\xa8S\x8a%I\xd8gI\x15\xe9\xe7$M\x15\xdc@\xa9\xa1@\x9c\xeee\xe0\xe0\xf76\xaa'
username = urllib.parse.quote(username)
password = urllib.parse.quote(password)
data = {
    "username": username,
    "password": password
}

response = requests.get(url, data=data)
print(response.text)