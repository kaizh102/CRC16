
PLY = 0x1021

print('             #########       CTC LOOKUP TABLE     ##############\ncrc_table = [', end='')
for i in range(0,0x100):
    crc = (i<<8) & 0xFFFF
    ply = PLY  # CRC-CCITT (XModem) Ploynomial

    for j in range (0, 8):
        if crc & 0x8000:
            crc = ((crc<<1) ^ ply) & 0xFFFF
        else:
            crc <<= 1
            crc & 0xFFFF
    print('0x{:04X}'.format(crc), end='')
    if i != 0xFF:
        print(', ', end='')
    else:
        print(']')
    if i%8 == 7:
        print('\n             ', end='')
print('#########  END OF CTC TABLE   ##############')
