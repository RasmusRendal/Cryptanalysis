#!/usr/bin/env python3
"""Module for miscellaneous classical ciphers"""

def rot(ciphertext: str, n: int = 13) -> str:
    """Uses the classical rot algorithm to encode a string

    Args:
        ciphertext: The string to decode
        n: How far to rotate
    """
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


def rot13(ciphertext: str) -> str:
    """The rot13 encoding.

    Shorthand for ``rot(ciphertext, 13)``
    """
    return rot(ciphertext, 13)
