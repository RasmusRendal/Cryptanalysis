import unittest
import sys, os
sys.path.append(os.path.dirname(__file__) + "/../../")
from Cryptanalysis import frequency

class test_frequency(unittest.TestCase):

    def test_count_occurences(self):
        text = "This is basically a long text, which has a bunch of characters in it. I could have just gone with lorem ipsum, but for some reason I didn't, and here I am, typing away at my keyboard for no good reason. I've had a pretty good day so far. It's a kinda gray weather outside, but I wouldn't have gone out anyway."
        occurences = {
                ' ': 61,
                '\'': 4,
                ',': 5,
                '.': 4,
                'I': 6,
                'T': 1,
                'a': 27,
                'b': 5,
                'c': 6,
                'd': 12,
                'e': 18,
                'f': 4,
                'g': 7,
                'h': 12,
                'i': 12,
                'j': 1,
                'k': 2,
                'l': 6,
                'm': 5,
                'n': 14,
                'o': 21,
                'p': 3,
                'r': 13,
                's': 13,
                't': 18,
                'u': 9,
                'v': 3,
                'w': 6,
                'x': 1,
                'y': 10
                }
        occurences2 = frequency.count_occurences(text)
        for o in occurences.keys():
            self.assertEqual(occurences[o], occurences2[o])


    def test_count_ngrams(self):
        text = "ATTACK"
        occurences = {
                "ATTA": 1,
                "TTAC": 1,
                "TACK": 1
                }
        self.assertEqual(frequency.count_ngrams(text, 4), (occurences, 3))

if __name__ == '__main__':
    unittest.main()
