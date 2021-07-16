import sys
import numpy as np

if __name__ == "__main__":
    a = []
    for l in sys.stdin:
        a.append(l.split())

    N = int(a[0][0])
    Q = int(a[1][0])

    matrix = np.empty(shape=(N, N), dtype=np.int64)

    for i in range(1, N+1):
        for j in range(1, N+1):
            matrix[i-1, j-1] = N * (i - 1) + (j - 1)

    for s in a[2:]:
        if len(s) == 3:
            s[1] = int(s[1]) - 1
            s[2] = int(s[2]) - 1
        if int(s[0]) == 1:
            if s[1] == s[2]:
                continue
            matrix[s[1], :], matrix[s[2], :] = matrix[s[2], :], matrix[s[1], :]

        if int(s[0]) == 2:
            if s[1] == s[2]:
                continue
            matrix[:, s[1]], matrix[:, s[2]] = matrix[:, s[2]], matrix[:, s[1]]

        if int(s[0]) == 3:
            matrix = matrix.T

        if int(s[0]) == 4:
            print(matrix[s[1], s[2]])