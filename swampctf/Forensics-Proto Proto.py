import socket

server = "chals.swampctf.com"
port = 44254 #UDP port

# Define flag.txt
# b"\x02" (command code)
# b"\x08" = len(flag.txt)
# b"\x66\x6c\x61\x67\x2e\x74\x78\x74" = flag.txt (HEX, ASCII encoding)
payload = b"\x02\x08\x66\x6c\x61\x67\x2e\x74\x78\x74"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(payload, (server, port))

response, addr = s.recvfrom(4096)
print("HEX response:", response.hex())
print("Decoded response:", response.decode(errors='ignore'))
s.close()

#HEX response: 077377616d704354467b723376337235335f6d795f70723037305f6c316b335f6d3037305f6d3037307d0a
#Decoded response: swampCTF{r3v3r53_my_pr070_l1k3_m070_m070}