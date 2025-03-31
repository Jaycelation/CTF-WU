import ast

def max_non_adjacent_sum(tokens):
    if not tokens:
        return 0
    if len(tokens) == 1:
        return tokens[0]

    prev2 = 0
    prev1 = 0

    for energy in tokens:
        current = max(prev1, prev2 + energy)
        prev2 = prev1
        prev1 = current

    return prev1

# Nhập danh sách từ người dùng
input_string = input()
try:
    tokens = ast.literal_eval(input_string)  # Chuyển đổi chuỗi thành danh sách Python
    if isinstance(tokens, list) and all(isinstance(x, int) for x in tokens):
        print(max_non_adjacent_sum(tokens))
    else:
        print("Lỗi: Vui lòng nhập một danh sách số nguyên hợp lệ.")
except (SyntaxError, ValueError):
    print("Lỗi: Định dạng đầu vào không hợp lệ.")
