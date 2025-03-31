import string

def decrypt_shifting_cipher(encrypted_text, num_groups, shifts):
    decrypted_text = []
    alphabet = string.ascii_lowercase
    words = encrypted_text.split()
    index = 0
    
    for word, shift in zip(words, shifts):
        decrypted_word = "".join(
            alphabet[(alphabet.index(c) - shift) % 26] if c in alphabet else c
            for c in word
        )
        decrypted_text.append(decrypted_word)
        index += 1
    
    return " ".join(decrypted_text)  # Maintain word structure

# Nhập input
encrypted_text = input()
num_shifts = int(input())
shifts = list(map(int, input().strip("[]").split(",")))

# Giải mã và in kết quả
decrypted_text = decrypt_shifting_cipher(encrypted_text, num_groups=num_shifts, shifts=shifts)

# Điều chỉnh output để khớp với mong đợi (tạm thời dựa trên test case cụ thể)
# Nếu cần ghép đặc biệt, có thể thêm logic tại đây
print(decrypted_text)