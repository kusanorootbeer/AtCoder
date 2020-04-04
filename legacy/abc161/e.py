def main():
    N, K, C = map(int, input().split())
    S = list(input())

    work = []
    for i, s in enumerate(S):
        if s == 'o':
            # work.append(i+1)
            work.append(i)
    # print(work)
    import itertools

    cand_list = []
    for v in itertools.combinations(work, K):
        cand = check1(v, C)
        if cand == -1:
            pass
        else:
            cand_list.append(cand)
    # print(cand_list)
    cand = cand_list[0]
    for c in cand:
        check(c, cand_list[1:])


def check(c, cand_list):
    for cand in cand_list:
        if c in cand:
            pass
        else:
            return -1
    print(c+1)


def check1(cand, C):
    num = len(cand)
    for i in range(num-1):
        if cand[i+1] - cand[i] < C+1:
            return -1
    return cand


if __name__ == '__main__':
    main()
