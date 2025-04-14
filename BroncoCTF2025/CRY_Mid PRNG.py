import z3

FLAG_LEN = 24
KNOWN_PLAINTEXT = [
    ord('b'), ord('r'), ord('o'), ord('n'), ord('c'), ord('o'), ord('{'),
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    ord('}')
]

ciphertexts_hex = [
    "411b54df7056d03168562a258086e59197f69c83e04d1f3c",
    "35776043e4fac40ddc7a5e3994ea716d631aa81f74e10b00",
    "4dffc89bbcf2acb5e4f236614ce259959b920047ace9e3b8",
    "84c0792ca53d8dd2cdade7f6f5cdd812126df1b075e6021f",
    "2d9fa83b9c928cd5c45216012c4239357b72e0e78c09c358",
    "b3013665420c524b1a0cc89fb21ca76b656cfeb952171d46",
    "7d2f782bac023ce5142246115cd2c9c5abc2b0f7bc997368",
    "c094dd7821a929c689f9c3a2f1d9fc86563955e4f172a60b",
    "387c4510190131eef1915b4ac971e4aeaed1cd8cc9dabe23",
    "f3c1762582cc928b5acc885ff2dce7aba52c3e7912575d06",
]

ciphertexts = [list(bytes.fromhex(x)) for x in ciphertexts_hex]

def extract_known(c):
    d = {}
    for i in range(FLAG_LEN):
        if KNOWN_PLAINTEXT[i] is not None:
            d[i] = c[i] ^ KNOWN_PLAINTEXT[i]
    return d

all_known = [extract_known(c) for c in ciphertexts]

def solve_lcg(runs):
    s = z3.Solver()
    a = z3.BitVec('a', 16)
    c = z3.BitVec('c', 16)
    for i, rd in enumerate(runs):
        X = [z3.BitVec(f'X_{i}_{j}', 16) for j in range(FLAG_LEN + 1)]
        for j in range(FLAG_LEN):
            s.add(X[j+1] == (a * X[j] + c) & 0xffff)
            if j in rd:
                s.add((X[j+1] & 0xff) == rd[j])
    if s.check() == z3.sat:
        m = s.model()
        return m[a].as_long(), m[c].as_long()
    return None

def rcv(cipher, av, cv):
    r0 = cipher[0] ^ ord('b')
    r1 = cipher[1] ^ ord('r')
    r6 = cipher[6] ^ ord('{')
    r23 = cipher[23] ^ ord('}')
    
    candidates = []
    for X1 in range(65536):
        if (X1 & 0xff) != r0:
            continue
        X2 = (av * X1 + cv) & 0xffff
        if (X2 & 0xff) != r1:
            continue
        Xc = X2
        valid = True
        for i in range(2, 24):
            Xc = (av * Xc + cv) & 0xffff
            if i == 6 and (Xc & 0xff) != r6:
                valid = False
                break
            if i == 23 and (Xc & 0xff) != r23:
                valid = False
        if valid:
            candidates.append(X1)
    
    if not candidates:
        return None
    
    Xc = candidates[0]
    out = []
    for i in range(FLAG_LEN):
        out.append(Xc & 0xff)
        Xc = (av * Xc + cv) & 0xffff
    
    return bytes(out[i] ^ cipher[i] for i in range(FLAG_LEN))

def main():
    res = solve_lcg(all_known)
    if res:
        a_val, c_val = res
        print("a=0x{:04x}, c=0x{:04x}".format(a_val, c_val))
        dec = rcv(ciphertexts[0], a_val, c_val)
        if dec:
            print(dec.decode(errors='ignore'))
        else:
            print("Decryption failed.")
    else:
        print("Could not solve LCG.")

if __name__ == "__main__":
    main()

# flag = bronco{0k_1ts_n0t_gr34t}