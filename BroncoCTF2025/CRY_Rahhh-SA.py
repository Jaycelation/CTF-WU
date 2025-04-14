from sympy import mod_inverse, isprime

def decrypt_rahhh_sa():
    e = 65537
    n = 3429719
    c = [-53102, -3390264, -2864697, -3111409, -2002688, -2864697, -1695722, -1957072,
         -1821648, -1268305, -3362005, -712024, -1957072, -1821648, -1268305, -732380,
         -2002688, -967579, -271768, -3390264, -712024, -1821648, -3069724, -732380,
         -892709, -271768, -732380, -2062187, -271768, -292609, -1599740, -732380,
         -1268305, -712024, -271768, -1957072, -1821648, -3418677, -732380, -2002688,
         -1821648, -3069724, -271768, -3390264, -1847282, -2267004, -3362005, -1764589,
         -293906, -1607693]
    p = -811
    
    q = n // abs(p)  
    if not isprime(q):
        print("q is not prime!")
        return
    print(f"p = {p}, q = {q}")
    
    phi_n = (abs(p) - 1) * (q - 1)
    print(f"phi(n) = {phi_n}")
    
    if e >= phi_n or phi_n % e == 0:
        print("Error: e not modular inverse!")
        return
    d = mod_inverse(e, phi_n)
    print(f"d = {d}")

    decrypted_chars = []
    for num in c:
        decrypted_value = pow(num % n, d, n)  
        if 0 <= decrypted_value < 256:  
            decrypted_chars.append(chr(decrypted_value))
        else:
            print(f"Warning: {decrypted_value} out range ASCII")
            decrypted_chars.append('?')
    
    decrypted_message = "".join(decrypted_chars)
    print("Decrypted message:")
    print(decrypted_message)
    
decrypt_rahhh_sa()

# flag = bronco{m4th3m4t1c5_r34l1y_1s_qu1t3_m4g1c4l_raAhH!}