import math
H = int(input())


def count(N):
    if N == 1:
        return 1
    else:
        return 2*count(math.floor(N/2)) + 1


print(count(H))
