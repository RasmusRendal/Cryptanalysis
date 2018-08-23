s2 = 'ff'*32

b2 = bytes.fromhex(s2)


def f(s):
    b1 = bytes.fromhex(s)
    return bytes(x ^ y for x, y in zip(b1, b2))
