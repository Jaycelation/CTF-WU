# Các giá trị bị mã hóa từ .data section
enc_values = [
    0xC5D9CACEC7EDFFE8,
    0xC5CAC7CEC8E2F4CE,
    0xDD9BE7F4CED2EED0,
]

enc_tail = [0xCF, 0xF4, 0xD6]  # 3 byte cuối

# Key XOR
key_8 = 0xABABABABABABABAB  # 8-byte XOR key
key_1 = 0xAB                # 1-byte XOR key

# Giải mã từng phần của flag
dec_values = [x ^ key_8 for x in enc_values]
dec_tail = [x ^ key_1 for x in enc_tail]

# Chuyển kết quả thành chuỗi ký tự
flag = "".join(map(lambda x: x.to_bytes(8, 'big').decode(errors='ignore'), dec_values))
flag += "".join(map(chr, dec_tail))

print("Correct Flag:", flag[::-1])
