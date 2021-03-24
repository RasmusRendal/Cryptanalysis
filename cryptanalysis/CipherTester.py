#!/usr/bin/python

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import argparse


def decode_fernet(key, text):
    f = Fernet(key)
    b = bytes(text, "utf-8")
    decrypted = f.decrypt(b)
    print("Fernat decryption:")
    print(decrypted)
    return decrypted


def decode_xor(key, text):
    key = bytes(key)
    text = bytes(text)
    output = bytearray()
    for i in range(len(text)):
        i2 = i
        while i2 > len(key)-1:
            i2 -= len(key)
        output.append(key[i2] ^ text[i])
    return output


def decode_rsa(key, text):
    priv_key = load_pem_private_key(
        bytes(key), password=None, backend=default_backend())
    plaintext = priv_key.decrypt(text, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    )
    print(plaintext)


def try_all(key, text, xor=True):
    if xor:
        print(decode_xor(key, text))

    try:
        print(decode_fernet(key, text))
    except:
        print("Fernet did not work")
    try:
        print(decode_rsa(key, text))
    except:
        print("RSA did not work")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Try decryption with a bunch of different algorithms')
    parser.add_argument('--key', dest='key', help='The encryption key')
    parser.add_argument('--text', dest='text', help='The encrypted text')

    args = parser.parse_args()

    if not args.key or not args.text:
        raise Exception("Key and text are needed")

    try_all(args.key, args.text)
