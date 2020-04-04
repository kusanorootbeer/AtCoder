def main():
    N = int(input())

    f = prime_factorize(N)
    print(f)
    # import collections
    # c = collections.Counter(f)
    # print(c)

    import itertools
    import numpy as np
    tmp = []
    for n in range(1, len(f)+1):
        for v in itertools.combinations(f, n):
            tmp.append(int(np.prod(v)))
    print(tmp)

    # for i in range(N):
    #     if i in tmp:
    #         pass
    #     if i
    co = 0
    import copy
    for k in range(2, N+1):
        print(k)
        n = copy.deepcopy(N)
        if k not in tmp:
            if n % k == 1:
                co += 1
        else:
            while True:
                if n % k == 0:
                    n = n//k
                else:
                    break
            if n % k == 1:
                co += 1
    print(co)

    # for k in range(2, N+1):
    #     n = copy.deepcopy(N)
    #     if k not in tmp:
    #         continue
    #     while True:
    #         if n % k == 0:
    #             n = n//k
    #         else:
    #             break
    #         # if n == 1:
    #         #     break
    #         # print(n, k)
    #     if n % k == 1:
    #         co += 1
    # print(co)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


if __name__ == '__main__':
    main()
