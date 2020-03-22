def main():
    import sys
    import math
    import itertools
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline
    N = int(input())

    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    l = itertools.combinations_with_replacement(b[:N], N)

    # K = math.factorial(N)
    # L = [0]*K
    # for i, v in enumerate(l):
    #     if i >= K:
    #         exit()
    #     print("".join(v))
    # L[i] = "".join(v)
    # print(L)

    num = (N)*(N+1)//2

    L = [['a']*N]*num

    L = [0]*N
    for i in range(1):
        L[N-i] = [i for i in range(j) for j in range(N)]
        print(L)
    # for i in range(num):

    base = ['a']*N

    check(base, 0, N)

    # for i in range():


# def back(keta, N):
#     for i in keta:


def check(l, layer, N):
    if layer == N-1:
        print("".join(l))
    for i in range(layer+1):
        l[layer-1] = chr(ord(l[layer-1])+1)
        check(l, layer+1, N)


if __name__ == '__main__':
    main()
