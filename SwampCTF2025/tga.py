def split_tga(input_file, output_file1, output_file2):
    with open(input_file, 'rb') as file:
        data = bytearray(file.read())

    header_size = 18

    # Lấy kích thước ảnh từ header
    width = int.from_bytes(data[12:14], byteorder='little')
    height = int.from_bytes(data[14:16], byteorder='little')

    # Tách dữ liệu ảnh
    image_data = data[header_size:]

    bytes_per_pixel = 3  # RGB (3 bytes mỗi pixel)

    # Chia dữ liệu thành 2 phần (dòng chẵn & dòng lẻ)
    image_data_odd = bytearray()
    image_data_even = bytearray()

    for y in range(height):
        start_idx = y * width * bytes_per_pixel
        end_idx = start_idx + width * bytes_per_pixel

        if y % 2 == 0:
            image_data_odd.extend(image_data[start_idx:end_idx])
        else:
            image_data_even.extend(image_data[start_idx:end_idx])

    # Tính lại chiều cao của từng ảnh con
    height_odd = (height + 1) // 2
    height_even = height // 2

    # Cập nhật header
    def update_header(header, new_height):
        new_header = bytearray(header)
        new_header[14:16] = new_height.to_bytes(2, byteorder='little')
        return new_header

    header_odd = update_header(data[:header_size], height_odd)
    header_even = update_header(data[:header_size], height_even)

    # Ghi file output
    with open(output_file1, 'wb') as file1:
        file1.write(header_odd)
        file1.write(image_data_odd)

    with open(output_file2, 'wb') as file2:
        file2.write(header_even)
        file2.write(image_data_even)

    print(f"Fichiers TGA séparés sauvegardés sous : {output_file1} et {output_file2}")

# Test lại
input_file = 'readbetweenthelines.tga'
output_file1 = 'cal_odd.tga'
output_file2 = 'chal_even.tga'

split_tga(input_file, output_file1, output_file2)
