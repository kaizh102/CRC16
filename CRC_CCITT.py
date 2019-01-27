from binascii import *
text ='00000000234'
msg = '313233343536373839'
msg += '0000'

ply = '1021'  # CRC-CCITT (XModem) Ploynomial

b_msg = unhexlify(msg)
if False:
    b_msg = text.encode() + b'\x00\x00'
b_ply = unhexlify(ply)

from pword import *
from bitarray import *

bit_msg = bitarray()
bit_ply = bitarray()
crc = bitarray()

bit_msg.frombytes(b_msg)
bit_ply.frombytes(b_ply)
pword(bit_msg)
crc.frombytes(unhexlify('FFFF'))
print('init:', end='')
pword(crc)

for i in range(0, len(bit_msg)):
    p = crc[0]
    crc = crc[1:]
    crc.append(bit_msg[i])
    print("  | {:1d}".format(p), end='')
    pword(crc)
    print("  |  ", end='')
    pword(bit_ply)
    print('...........')
    if p:
        crc ^= bit_ply
    print("   <-".format(p), end='')
    pword(crc)
if p:
    crc ^= bit_ply

