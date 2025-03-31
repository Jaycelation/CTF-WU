# Dữ liệu từ binary
xormask = [
    0x4B7AB17E1180469A, 0xEA141BB0ACF3BE01,
    0x5BF248F39C3FAD27, 0xE7018EA842637EFC,
    0x1219C03F5A27A525, 0x99A92A7C03F1C6DA
]

fmsg = [
    0x2508D01B7DC612D9, 0xB57F7ADDDF92F37A,
    0x28812D81E84DC261, 0x745B4FA3F39D0001
]

# Chuyển đổi `xormask` và `fmsg` thành mảng bytes
xormask_bytes = b''.join(x.to_bytes(8, 'little') for x in xormask)[:31]
fmsg_bytes = b''.join(x.to_bytes(8, 'little') for x in fmsg)

# Giải mã flag bằng XOR
flag_bytes = bytes([x ^ y for x, y in zip(xormask_bytes, fmsg_bytes)])
print(flag_bytes.decode('utf-8', errors='ignore'))
