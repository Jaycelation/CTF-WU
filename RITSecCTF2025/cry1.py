import ast
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Đọc dữ liệu từ tales.txt
with open('tales.txt', 'r') as f:
    data = f.readlines()

# Trích xuất scrambled_message và enc_flag
scrambled_message = ast.literal_eval(data[0].split('=')[1].strip())
enc_flag_raw = data[1].split('=')[1].strip()
enc_flag = bytes.fromhex(enc_flag_raw.strip("'").strip("\""))

n = 0x1337
e = 0x10001

def inverse_scramble(b, a):
    """Đảo ngược quá trình scramble."""
    inv_a = [0] * len(a)
    for i, v in enumerate(a):
        inv_a[v] = i
    return [b[inv_a[i]] for i in range(len(a))]

def inverse_super_scramble(b, e):
    """Đảo ngược quá trình super_scramble."""
    a = list(range(n))
    rev_steps = []
    while e:
        if e & 1:
            rev_steps.append(a[:])
        a = inverse_scramble(a, a)
        e >>= 1
    
    for step in reversed(rev_steps):
        b = inverse_scramble(b, step)
    return b

# Khôi phục message ban đầu
original_message = inverse_super_scramble(scrambled_message, e)

# Tạo khóa AES
key = sha256(str(original_message).encode()).digest()

# Giải mã flag
cipher = AES.new(key, AES.MODE_ECB)
flag = unpad(cipher.decrypt(enc_flag), 16)

print(flag.decode())