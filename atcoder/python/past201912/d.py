import sys

def solution(input_list):
    elem_num = input_list[0]
    elements = input_list[1:]

    if elem_num == len(set(elements)):
        return 'Correct'

    li = [0 for x in range(elem_num + 1)] # 0-index なのでやりやすさのために + 1
    
    for elem in elements:
        li[elem] += 1
        
    li = li[1:] # 0-index なので最初（0番目）は除く
    miss = int(li.index(0)) + 1
    dup = int(li.index(2)) + 1

    return str(dup)+' '+str(miss)

if __name__ == "__main__":
    input_list = []
    for l in sys.stdin:
        input_list.append(int(l))

    print(solution(input_list))
