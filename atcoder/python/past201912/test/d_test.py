import unittest
import sys
import os
sys.path.append(os.getcwd())
from d import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):

        input_list = [
            [6,1,5,6,3,2,6],
            [7,5,4,3,2,7,6,1]
        ]

        expects = [
            '6 4',
            'Correct'
        ]

        for i in range(len(input_list)):
            print(f'{i+1} th test case / total {len(input_list)}')
            self.assertEqual(expects[i], solution(input_list[i]))

if __name__ == "__main__":
    unittest.main()