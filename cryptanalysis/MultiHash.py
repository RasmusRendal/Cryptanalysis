#!/usr/bin/python

import argparse
import crypt_common
import hashlib
import base64

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run all known hashing algorithms on string')
    parser = crypt_common.add_parser_args(parser)
    args = parser.parse_args()
    text = crypt_common.get_text(args)
    textBytes = bytes(text, 'utf-8')
    print("Hashing " + text)
    Already_Tried = []
    for algorithm in hashlib.algorithms_available:
        if algorithm.lower() not in Already_Tried:
            try:
                func = getattr(hashlib, algorithm.lower())
                hashDigest = func(textBytes).digest()
                b64 = base64.b64encode(hashDigest).decode()
                print(algorithm + ': ' + " "*(10-len(algorithm)) + b64)
                Already_Tried.append(algorithm.lower())
            except TypeError:
                pass
            except AttributeError:
                pass
