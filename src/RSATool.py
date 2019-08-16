#!/usr/bin/python
#RSA Solver by Rasmus Rendal

import argparse
import numpy
import math


def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y


def i2osp(x, xLen):
        digits = []

        while x:
            digits.append(int(x % 256))
            x //= 256
            digits.append(0)
        return digits[::-1]

def os2ip(X):
        xLen = len(X)
        X = X[::-1]
        x = 0
        for i in range(xLen):
            x += X[i] * 256^i
        return x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def chinese_remainder(p, q, dp, dq, c):
    #q_inv = pow(q,-1) % p
    #q_inv = modinv(p, q)
    q_inv = f(q, p-2, p)
    print(type(q_inv))
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (q_inv * (m1 - m2)) % p
    m = m2 + h*q
    to_string(m, p*q)
    print(m)

def to_string(m, n):
    keyLength = n.bit_length()+5
    string = i2osp(m, keyLength)
    for n in string:
        if n != 0:
            c = chr(n)
            print(c, end='')
            #print(hex(n), end='')
    print('')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool for solving RSA encryption")
    parser.add_argument('--c', dest='c', type=int, nargs=1)
    parser.add_argument('--p', dest='p', type=int, nargs=1)
    parser.add_argument('--q', dest='q', type=int, nargs=1)
    parser.add_argument('--dp', dest='dp', type=int, nargs=1)
    parser.add_argument('--dq', dest='dq', type=int, nargs=1)
    args = parser.parse_args()
    if not args.c:
        raise Exception("Message is required")
    c = args.c[0]
    if args.c and args.p and args.q and args.dp and args.dq:
        chinese_remainder(args.p[0], args.q[0], args.dp[0], args.dq[0], args.c[0])
