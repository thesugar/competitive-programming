import unittest
import sys
import os
sys.path.append(os.getcwd())
from c import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):

        input_list = [
            [4, 18, 25, 20, 9, 13],
            [95, 96, 97, 98, 99,100],
            [19, 92, 3, 35, 78, 1]
        ]

        expects = [
            18,
            98,
            35
        ]

        for i in range(len(input_list)):
            print(f'{i+1} th test case / total {len(input_list)}')
            self.assertEqual(expects[i], solution(input_list[i]))

if __name__ == "__main__":
    unittest.main()