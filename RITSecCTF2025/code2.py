from ast import literal_eval

def find_combination(subarrays, target, index=0, current_combination=[]):
    if index == len(subarrays):
        if sum(current_combination) == target:
            return current_combination
        return None
    
    for num in subarrays[index]:
        result = find_combination(subarrays, target, index + 1, current_combination + [num])
        if result:
            return result
    return None

# Đọc dữ liệu đầu vào
subarrays = literal_eval(input().strip())  # Chuyển đổi chuỗi đầu vào thành danh sách
T = int(input().strip())

# Tìm và in ra kết quả
result = find_combination(subarrays, T)
print(result)
