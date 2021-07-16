import sys
import numpy as np

def solution(a):

    N = int(a[0])

    if N == 1:
        return a[1]
    
    # a[1], a[2], ..., a[N] のそれぞれは文字列
    ans = [''] * N

    for i in range(1, int(N) +1):
        if i >= (N + 1) / 2:
            break

        intersection = set(a[i]) & set(a[N+1-i])
        if len(intersection) == 0:
            return -1
        
        ans[i-1] = list(intersection)[0]
        ans[-i] = list(intersection)[0]
    
    if N % 2 != 0:
        print(f'ans is {ans}')
        print(f'a is {a}')
        print(f'a[int((N+1)/2) + 1][0] is {a[int((N+1)/2) + 1][0]}')
        ans[int((N+1)/2)] = a[int((N+1)/2) + 1][0]

    return ''.join(ans)

if __name__ == "__main__":
    a = []
    for l in sys.stdin:
        a.append(l.replace('\n', ''))

    print(solution(a))
