from hashlib import md5, sha256, sha512

target_hash = bytes.fromhex("f600d59a5cdd245a45297079299f2fcd811a8c5461d979f09b73d21b11fbb4f899389e588745c6a9af13749eebbdc2e72336cc57ccf90953e6f9096996a58dcc")

f = open("passwords_10.txt", "r")
for i in range(10000):
    try:
        p = f.readline().strip().encode()
    except:
        continue

    flag = b"swampCTF{" + p + b"}"
    h = flag

    for i in range(100):
        h = md5(h).digest()
    for i in range(100):
        h = sha256(h).digest()
    for i in range(100):
        h = sha512(h).digest()

    if h == target_hash:
        print(flag.decode())
#swampCTF{secretcode}