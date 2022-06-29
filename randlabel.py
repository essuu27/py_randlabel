from random import randint

def randlabel(x: int):
    chars = ''.join(chr(i) + chr(i + 32) for i in range(65, 91)) + '0123456789'
    return ''.join(chars[randint(0, 61)] for _ in range(x))
