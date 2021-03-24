def rot(ciphertext, n=13):
    out = ""
    for c in ciphertext:
        v = ord(c)
        upper = True
        if v >= ord('a'):
            v -= ord('a') - ord('A')
            upper = False

        if not (v >= ord('A') and v <= ord('Z')):
            out += c
            continue

        v -= ord('A')
        v += n
        v %= ord('Z') - ord('A')+1
        if upper:
            v += ord('A')
        else:
            v += ord('a')
        out += chr(v)
    return out


def rot13(ciphertext):
    return rot(ciphertext, 13)
