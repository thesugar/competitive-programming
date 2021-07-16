import sys
import numpy as np
from operator import mul

def solution(input_list):

    N, M, Q = input_list[0]

    users = np.zeros((N, M), np.int8)
    questions = np.ones(M, np.int32) * N

    for s in range(1, Q+1):

        log = input_list[s]

        if log[0] == 1:
            print(np.dot(users[log[1]-1], questions))

        if log[0] == 2:
            # log[1] solved log[2]
            users[log[1]-1][log[2]-1] = 1
            questions[log[2]-1] -= 1

if __name__ == "__main__":
    stdin = []
    for l in sys.stdin:
        stdin.append([int(x) for x in l.split()])
    
    solution(stdin)
