import unittest
import random
from Cryptanalysis import aes

class TestXOR(unittest.TestCase):

    def test_subBytes(self):
        state = []
        for i in range(random.randint(2, 20)):
            state.append([])
            for j in range(random.randint(2, 20)):
                state[i].append(random.randint(0, 255))
        self.assertEqual(aes.inv_subBytes(aes.subBytes(state)), state)

    def test_shiftRows(self):
        state = [
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3]
                ]
        finished_state = [
                [0, 1, 2, 3],
                [1, 2, 3, 0],
                [2, 3, 0, 1],
                [3, 0, 1, 2]
                ]
        self.assertEqual(aes.shiftRows(state), finished_state)
        self.assertEqual(aes.inv_shiftRows(aes.shiftRows(state)), state)

if __name__ == '__main__':
    unittest.main()
