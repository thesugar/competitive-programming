import sys
import numpy as np

if __name__ == "__main__":
    a = []
    for l in sys.stdin:
        a.append(l.replace('\n', ''))
    # a: ['5 3', '1 1 0', '1 2 0', '2 2 4']

    list_ = np.arange(1, int(a[0].split()[0])+1)

    for line in a[1:]:
        line = line.split()
        if int(line[0]) == 1:
            to_change = int(line[1]) - 1
            list_[to_change], list_[to_change+1] = list_[to_change+1], list_[to_change]

        if (int(line[0])) == 2:
            sort_from = int(line[1]) - 1
            sort_to = int(line[2]) - 1
            list_[sort_from:sort_to + 1] = sorted(list_[sort_from:sort_to + 1])

    print(' '.join(str(list_)[1:-1].split()))
