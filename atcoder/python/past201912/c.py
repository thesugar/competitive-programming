def solution(input_list):
    return sorted(input_list, reverse=True)[2]

if __name__ == "__main__":
    input_list = list(map(int,input().split()))
    print(solution(input_list))
