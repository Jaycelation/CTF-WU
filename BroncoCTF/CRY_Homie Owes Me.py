import itertools
import hashlib

# homie:ea23f261fff0ebc5b0a5d74621218e413a694ed0815a90615cf6edd7b49e6d0d

leet_dict = {
    'a': '4', 'b': '8', 'c': '<', 'e': '3', 'g': '6', 'h': '#', 'i': '1',
    'l': '1', 'o': '0', 's': '5', 't': '7', 'z': '2'
}

target_hash = 'ea23f261fff0ebc5b0a5d74621218e413a694ed0815a90615cf6edd7b49e6d0d'

original_str = list("yoshiethehomie")

# Define the replaceable positions as (index, original_char, substitution)
replaceable = [
    (1, 'o', leet_dict['o']),
    (2, 's', leet_dict['s']),
    (3, 'h', leet_dict['h']),
    (4, 'i', leet_dict['i']),
    (5, 'e', leet_dict['e']),
    (6, 't', leet_dict['t']),
    (7, 'h', leet_dict['h']),
    (8, 'e', leet_dict['e']),
    (9, 'h', leet_dict['h']),
    (10, 'o', leet_dict['o']),
    (12, 'i', leet_dict['i']),
    (13, 'e', leet_dict['e']),
]

found = False

for bits in itertools.product([0, 1], repeat=len(replaceable)):
    temp = original_str.copy()
    for i, bit in enumerate(bits):
        if bit:
            idx, orig, sub = replaceable[i]
            temp[idx] = sub
    leet_str = ''.join(temp)
    
    special_positions = []
    for idx, c in enumerate(leet_str):
        if c == 's':
            special_positions.append((idx, '$'))
        elif c == 'i':
            special_positions.append((idx, '!'))
    
    if not special_positions:
        continue  
    
    for pos, replacement in special_positions:
        special_str = leet_str[:pos] + replacement + leet_str[pos+1:]
        
        for num in range(10000):
            candidate = f"{special_str}{num:04}"
            flag = f"bronco{{{candidate}}}"
            hash_obj = hashlib.sha256(flag.encode()).hexdigest()
            if hash_obj == target_hash:
                print(f"Found flag: {flag}")
                found = True
                exit()
    
if not found:
    print("All possibilities exhausted.")
# flag = bronco{y0sh1eth3hom!e8778}