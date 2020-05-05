import numpy as np


def main():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input().split()[0])
    B = []
    for i in range(N):
        B.append(int(input().split()[0]))

    A = np.array(A)
    A_clear = np.zeros_like(A)
    for b in B:
        A_clear += 1 * (A == b)
#  print(A)
#  print(A_clear)
    bingo_c(A_clear)


def bingo_c(arr):
    if (np.sum(arr, axis=0) == 3).any():
        print('Yes')
    elif (np.sum(arr, axis=1) == 3).any():
        print('Yes')
    elif arr[0, 0]+arr[1, 1]+arr[2, 2] == 3:
        print('Yes')
    elif arr[0, 2]+arr[1, 1]+arr[2, 0] == 3:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
