import itertools

#Runs an xor on the two bytes objects
def xor(string, key):
    bytes_return = bytearray()
    for i in zip(string, itertools.cycle(key)):
        bytes_return.append(i[0]^i[1])
    return bytes(bytes_return)


