import sys
import numpy as np

if __name__ == "__main__":
    stdin = []
    for l in sys.stdin:
        stdin.append([x for x in l.split()])

    N = int(stdin[0][0])

    for i in range(1, 6):
        stdin[i][0] = stdin[i][0].replace('.', str(0)).replace('#', str(1))

    input_ = np.array(stdin[1:])
    answer = []

    for num in range(1, N+1): # num: 何文字目
        signal = input_[0][0][4*(num-1): 4*num] + input_[1][0][4*(num-1): 4*num] + input_[2][0][4*(num-1): 4*num] + input_[3][0][4*(num-1): 4*num]

        if signal == '0111010101010101':
            answer.append(0)

        if signal == '0010011000100010':
            answer.append(1)

        if signal == '0111000101110100':
            answer.append(2)

        if signal == '0111000101110001':
            answer.append(3)

        if signal == '0101010101110001':
            answer.append(4)

        if signal == '0111010001110001':
            answer.append(5)

        if signal == '0111010001110101':
            answer.append(6)

        if signal == '0111000100010001':
            answer.append(7)

        if signal == '0111010101110101':
            answer.append(8)

        if signal == '0111010101110001':
            answer.append(9)

    print(''.join([str(x) for x in answer]))