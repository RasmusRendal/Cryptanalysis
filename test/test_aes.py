import os, sys
sys.path.append(os.path.dirname(__file__) + "/../")
from cryptanalysis import aes
import unittest
import random


class TestAES(unittest.TestCase):

    def test_subBytes(self):
        state = []
        for i in range(random.randint(2, 20)):
            state.append([])
            for j in range(random.randint(2, 20)):
                state[i].append(random.randint(0, 255))
        self.assertEqual(aes.invSubBytes(aes.subBytes(state)), state)

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
        self.assertEqual(state[3][3], 3)
        self.assertEqual(aes.invShiftRows(aes.shiftRows(state)), state)
        self.assertEqual(aes.invShiftRows(finished_state), state)

    def test_MixCol(self):
        ins = [
            [219, 19, 83, 69],
            [242, 10, 34, 92],
            [1, 1, 1, 1],
            [198, 198, 198, 198],
            [212, 212, 212, 213],
            [45, 38, 49, 76]
        ]
        outs = [
            [142, 77, 161, 188],
            [159, 220, 88, 157],
            [1, 1, 1, 1],
            [198, 198, 198, 198],
            [213, 213, 215, 214],
            [77, 126, 189, 248]
        ]
        for i in range(len(ins)):
            self.assertEqual(aes.mixCol(ins[i]), outs[i])

    def testInv_mixCol(self):
        ins = [
            [219, 19, 83, 69],
            [242, 10, 34, 92],
            [1, 1, 1, 1],
            [198, 198, 198, 198],
            [212, 212, 212, 213],
            [45, 38, 49, 76]
        ]
        for i in ins:
            self.assertEqual(aes.invMixCol(aes.mixCol(i)), i)

    def testToBytes(self):
        self.assertEqual(b"a"*16, aes.block2bytes(aes.bytes2block(b"a"*16)))

    def testMixCols(self):
        state = [
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3]
        ]
        self.assertEqual(aes.invMixCols(aes.mixCols(state)), state)



if __name__ == '__main__':
    unittest.main()
