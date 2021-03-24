#!/usr/bin/env python3
import os, sys
sys.path.append(os.path.dirname(__file__) + "/../")
from cryptanalysis import substitution
import unittest


class TestXOR(unittest.TestCase):

    def test_substitution_solver(self):
        plaintext = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. My dear Mr. Bennet, said his lady to him one day, have you heard that Netherfield Park is let at last? Mr. Bennet replied that he had not. But it is, returned she; for Mrs. Long has just been here, and she told me all about it. Mr. Bennet made no answer. Do you not want to know who has taken it?” cried his wife impatiently."

        alphabet = {
            'a': 'b',
            'b': 'z',
            'c': 'e',
            'd': 'f',
            'e': 'h',
            'f': 'z',
            'g': 'g',
            'h': 'c',
            'i': 'i',
            'j': 'j',
            'k': 'p',
            'l': 'm',
            'm': 'l',
            'n': 'n',
            'o': 's',
            'p': 'k',
            'q': 'q',
            'r': 'r',
            's': 'o',
            't': 't',
            'u': 'u',
            'v': 'v',
            'w': 'w',
            'x': 'x',
            'y': 'y',
            'z': 'f'
        }

        ciphertext = substitution.substitution_decode(plaintext, alphabet)

        self.assertEqual(substitution.substitution_solve(
            ciphertext)[0], plaintext)


if __name__ == '__main__':
    unittest.main()
