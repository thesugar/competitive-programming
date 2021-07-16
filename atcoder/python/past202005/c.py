import numpy as np

def solution(A, R, N):

    prev = A
    if R == 1:
        return A
        
    for i in range(1, N):
        prev = prev * R
        if prev > 10 ** 9:
            return 'large'
        
    return prev

if __name__ == "__main__":
    A, R, N = list(map(int,input().split()))

    print(solution(A, R, N))