import os, sys
sys.path.append(os.path.dirname(__file__) + "/../")
from cryptanalysis import xor
import unittest


class TestXOR(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(xor.xor(b'a', b'a'), b'\x00')
        self.assertEqual(xor.xor(b'\x12\x57\x25\x39\x87\x13\x26\x54',
                                 b'\x12\x45\x68\x78\x35\x15\x97\x12'), b'\x00\x12\x4d\x41\xb2\x06\xb1\x46')
        self.assertEqual(xor.xor(b'yyyyyyyyyy', b'y'),
                         b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(xor.xor(b'a', b'abe'), b'\x00')
        self.assertEqual(xor.xor("abe", b'abe'), b'\x00\x00\x00')

    def test_get_hamming_distance(self):
        self.assertEqual(xor.get_hamming_distance(b"ee", b"ff"), 4)
        self.assertEqual(xor.get_hamming_distance(
            b"this is a test", b"wokka wokka!!!"), 37)


if __name__ == '__main__':
    unittest.main()
