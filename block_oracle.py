import forge
import sys
from crypto import decrypt
from hexdump import hexdump

def decode_blocks(blocks, decrypt_func):
    toWrite = b''
    for block in blocks:
        toWrite += block
    decrypted = decrypt_func(toWrite)
    decrypted_blocks = list(decrypted[i:16+i] for i in range(0, len(decrypted), 16))
    return decrypted_blocks


def modify_text(ciphertext, plaintext, decrypt_func, new_plaintext):
    #The encrypted message as blocks
    blocks = list(ciphertext[i:16+i] for i in range(0, len(ciphertext), 16))

    # Plaintext and the plaintext we want as blocks
    plain_blocks = list(plaintext[i:16+i] for i in range(0, len(plaintext), 16))
    adv_blocks = list(new_plaintext[i:16+i] for i in range(0, len(new_plaintext), 16))

    # Add padding to the last block, and convert to bytes
    for i in range(len(plain_blocks)):
        plain_blocks[i] = bytes(plain_blocks[i], 'ascii')
    for i in range(len(adv_blocks)):
        adv_blocks[i] = bytes(adv_blocks[i], 'ascii')
    adv_blocks[-1] = forge.pad(adv_blocks[-1])
    plain_blocks[-1] = forge.pad(plain_blocks[-1])

    # Start out with using the normal one
    new_enc = blocks

    # Replace the second to last encrypted block with something that'll be CBC'ed into the plaintext we want on the last block
    new_enc[-2] = (forge.byte_xor(forge.byte_xor(adv_blocks[-1], plain_blocks[-1]), blocks[-2]))

    #We now have to decrypt this message, to see what the second to last plain block looks like, so we know how to modify the third to last
    decrypted_blocks = decode_blocks(new_enc, decrypt_func)
    new_enc[-3] = (forge.byte_xor(forge.byte_xor(adv_blocks[-2], decrypted_blocks[-2]), blocks[-3]))

    # And so on
    decrypted_blocks = decode_blocks(new_enc, decrypt_func)
    new_enc[-4] = (forge.byte_xor(forge.byte_xor(adv_blocks[-3], decrypted_blocks[-3]), blocks[-4]))

    # And this is actually the IV
    decrypted_blocks = decode_blocks(new_enc, decrypt_func)
    new_enc[-5] = (forge.byte_xor(forge.byte_xor(adv_blocks[-4], decrypted_blocks[-4]), blocks[-5]))

    toWrite = b''
    for block in new_enc:
        toWrite += block
    return toWrite
