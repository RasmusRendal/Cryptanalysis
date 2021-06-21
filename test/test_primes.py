#!/usr/bin/env python3
import os, sys
sys.path.append(os.path.dirname(__file__) + "/../")
from cryptanalysis import primes
import unittest

class TestPrimes(unittest.TestCase):

    def test_isprime(self):
        self.assertFalse(primes.prime_check(-3))
        self.assertFalse(primes.prime_check(1))
        self.assertTrue(primes.prime_check(2))
        self.assertTrue(primes.prime_check(3))
        self.assertFalse(primes.prime_check(4))
        self.assertTrue(primes.prime_check(5))
        self.assertFalse(primes.prime_check(6))
        self.assertFalse(primes.prime_check(306))
        self.assertTrue(primes.prime_check(307))


    def test_nextPrime(self):
        self.assertEqual(primes.next_prime(2), 2)
        self.assertEqual(primes.next_prime(4), 5)
        self.assertEqual(primes.next_prime(8), 11)

if __name__ == '__main__':
    unittest.main()
