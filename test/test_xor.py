import unittest
from Cryptanalysis import xor

class TestXOR(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(xor.xor(b'a', b'a'), '\x00')
        self.assertEqual(xor.xor(b'\x12\x57\x25\x39\x87\x13\x26\x54', b'\x12\x45\x68\x78\x35\x15\x97\x12'), '\x00\x12\x4d\x41\xb2\x06\xb1\x46')
        self.assertEqual(xor.xor(b'yyyyyyyyyy', b'y'), '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(xor.xor(b'a', b'abe'), '\x00')

    def test_get_hamming_distance(self):
        self.assertEqual(xor.get_hamming_distance("ee", "ff"), 4)
        self.assertEqual(xor.get_hamming_distance("this is a test", "wokka wokka!!!"), 37)


if __name__ == '__main__':
    unittest.main()
