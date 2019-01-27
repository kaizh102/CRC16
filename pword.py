from binascii import *
def pword(word):
    for j,b in zip(range(0,16), word):
        if (j%4) == 0:
            print(' ', end='')
        print('{:1d}'.format(word[j]), end='')
    print(' ', hexlify(word.tobytes()))
