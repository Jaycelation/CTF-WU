from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy

e = 3
ct = 219878849218803628752496734037301843801487889344508611639028
n = 245841236512478852752909734912575581815967630033049838269083

# Find the m (plaintext message) by extracting the e-th root of the ciphertext
m = sympy.root(ct, e)

print(long_to_bytes(219878849218803628752496734037301843801487889344508611639028))
