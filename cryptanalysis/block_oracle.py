import sys
import xor


def decode_blocks(blocks, decrypt_func, block_len):
    toWrite = b''
    for block in blocks:
        toWrite += block
    decrypted = decrypt_func(toWrite)
    decrypted_blocks = list(decrypted[i:block_len+i]
                            for i in range(0, len(decrypted), block_len))
    return decrypted_blocks


def pad(block, length):
    missing = length-len(block)
    block = bytes(block.decode('utf-8') + chr(missing)*missing, 'ascii')
    return block


def modify_text(ciphertext, plaintext, decrypt_func, new_plaintext, block_len):
    # The encrypted message as blocks
    blocks = list(ciphertext[i:block_len+i]
                  for i in range(0, len(ciphertext), block_len))

    # Plaintext and the plaintext we want as blocks
    plain_blocks = list(plaintext[i:block_len+i]
                        for i in range(0, len(plaintext), block_len))
    adv_blocks = list(new_plaintext[i:block_len+i]
                      for i in range(0, len(new_plaintext), block_len))

    # Add padding to the last block, and convert to bytes
    for i in range(len(plain_blocks)):
        plain_blocks[i] = bytes(plain_blocks[i], 'ascii')
    for i in range(len(adv_blocks)):
        adv_blocks[i] = bytes(adv_blocks[i], 'ascii')
    adv_blocks[-1] = pad(adv_blocks[-1], block_len)
    plain_blocks[-1] = pad(plain_blocks[-1], block_len)

    # Start out with using the normal one
    new_enc = blocks

    for i in range(1, len(plain_blocks)+1):
        # Replace the second to last encrypted block with something that'll be CBC'ed into the plaintext we want on the last block
        new_enc[-1-i] = (xor.xor(xor.xor(adv_blocks[-i],
                                         plain_blocks[-i]), blocks[-1-i]))
        plain_blocks = decode_blocks(new_enc, decrypt_func, block_len)

    toWrite = b''
    for block in new_enc:
        toWrite += block
    return toWrite
