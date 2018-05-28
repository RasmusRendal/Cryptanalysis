#!/usr/bin/python

from cryptography.fernet import Fernet
import argparse
import crypt_common

def decode_fernet(key, text):
    f = Fernet(key)
    b = b"gAAAAABaDDCRPXCPdGDcBKFqEFz9zvnaiLUbWHqxXqScTTYWfZJcz-WhH7rf_fYHo67zGzJAdkrwATuMptY-nJmU-eYG3HKLO9WDLmO27sex1-R85CZEFCU="
    b = bytes(text, "utf-8")
    decrypted = f.decrypt(b)
    print("Fernat decryption:")
    print(decrypted)
    return decrypted


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Try decryption with a bunch of different algorithms')
    parser.add_argument('--key', dest='key', help='The encryption key')
    parser.add_argument('--text', dest='text', help='The encrypted text')

    args = parser.parse_args()

    if not args.key or not args.text:
        raise Exception("Key and text are needed")

    decode_fernet(args.key, args.text)
