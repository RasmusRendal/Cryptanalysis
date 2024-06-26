from __future__ import division
import itertools
import fitness


def get_hamming_distance(s1: bytes, s2: bytes) -> int:
    """Compute the hamming distance between two bytestrings

    The Hamming distance is the number of bits that differ
    between the two strings.

    Returns:
        int"""
    assert(len(s1) == len(s2))
    distance = 0
    for c in zip(s1, s2):
        c0 = bin(c[0])[2:]
        c1 = bin(c[1])[2:]
        c0 = "0"*(8-len(c0)) + c0
        c1 = "0"*(8-len(c1)) + c1
        distance += sum(b0 != b1 for b0, b1 in zip(c0, c1))
    return distance


def get_keysize_candidates(ciphertext: bytes, candidate_num: int = 4, range_min: int = 1, range_max: int = 40):
    best_keysizes = {}
    for n in range(range_min, min(range_max, int(len(ciphertext)/2))):
        ranges = list(ciphertext[i:i+n] for i in range(0, len(ciphertext), n))
        distances = []
        for i in range(0, len(ranges), 2):
            try:
                r1 = ranges[i]
                r2 = ranges[i+1]
                distances.append(get_hamming_distance(r1, r2))
            except (IndexError, AssertionError):
                pass

        n_distance = sum(distances)/len(distances)
        n_distance = n_distance/n
        if len(best_keysizes) < candidate_num:
            best_keysizes[n] = n_distance
        else:
            for i in best_keysizes.keys():
                if best_keysizes[i] > n_distance:
                    best_keysizes.pop(i)
                    best_keysizes[n] = n_distance
                    break
    return best_keysizes.keys()


def mgram_fitness(ciphertext, probs):
    return fitness.ngram_fitness(ciphertext, probs, n=1)


def vary_xor_key(ciphertext: bytes, key: bytes, probs) -> bytes:
    for c in range(len(key)):
        alt_keys = []
        for i in range(255):
            new_key = list(key)
            new_key[c] = chr(i)
            alt_keys.append("".join(new_key))
        key = fitness.get_highest_fitness(ciphertext, alt_keys, xor)
    return key


def break_repeating_xor(ciphertext: bytes, qprobs=None, mprobs=None) -> bytes:
    """Breaks the repeating XOR/Vigenère cipher

    Args:
        ciphertext (bytes): Your ciphertext
    """

    if qprobs == None:
        qprobs = fitness.get_probs()
    if mprobs == None:
        mprobs = fitness.get_probs(n=1)

    keysize_candidates = get_keysize_candidates(ciphertext, candidate_num=10)
    keys = []
    cur_key = 0

    single_xor_keys = []
    for i in range(255):
        single_xor_keys.append([chr(i)])

    for n in keysize_candidates:
        keys.append('')
        blocks = list(ciphertext[i:n+i] for i in range(0, len(ciphertext), n))
        # Break the ciphertext into blocks, and solve them one char at a time
        for i in range(n):
            block_i = b''.join([blocks[i] for i in range(len(blocks))])
            highest_cur_key = fitness.get_highest_fitness(
                block_i, single_xor_keys, xor, fitness_func=mgram_fitness, probs=mprobs)
            keys[cur_key] += highest_cur_key[0]
        cur_key += 1
    highest_key = fitness.get_highest_fitness(
        ciphertext, keys, xor, fitness_func=fitness.ngram_fitness, probs=qprobs)
    return vary_xor_key(ciphertext, highest_key, qprobs)


def xor(plaintext: bytes, key: bytes, loop=True):
    """Takes the XOR of a string using key.

    If the string is longer than the key, the
    key is repeated to fit. The function
    also accepts strings

    Args:
        plaintext: The plaintext
        key: The key

    Returns:
        bytes: The de/en-crypted text"""
    if not loop:
        assert len(plaintext) == len(key), "Loop is disabled, and plaintext is " + str(len(plaintext)) + " while key is " + str(len(key))
    bytes_return = bytearray()
    for i in zip(plaintext, itertools.cycle(key)):
        i0 = i[0]
        i1 = i[1]
        if type(i0) is str:
            i0 = ord(i0)
        if type(i1) is str:
            i1 = ord(i1)
        bytes_return.append(i0 ^ i1)
    return bytes(bytes_return)
