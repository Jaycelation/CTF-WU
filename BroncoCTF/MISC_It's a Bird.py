# steghide extract -sf myBirb.jpg to convert .csv file
# R column / MSG 6

ascii_values = [98, 114, 111, 110, 99, 111, 123, 105, 60, 51, 112, 108, 97, 110, 101, 115, 125]

decoded_message = ''.join(chr(i) for i in ascii_values)

print("Decoded Message:", decoded_message)
# flag = bronco{i<3planes}