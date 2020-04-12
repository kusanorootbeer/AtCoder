def main():
    N = int(input())
    S = list(input())

    # su = 0
    # for i, si in enumerate(S):
    #     for j, sj in enumerate(S[i+1:]):
    #         if si == sj:
    #             continue
    #         for k, sk in enumerate(S[i+j+2:]):
    #             # print(si, sj, sk)
    #             # print(i+1, j+i+2, k+j+i+2)
    #             if j == k:
    #                 continue
    #             elif sj != sk and si != sk:
    #                 su += 1
    # print(su)

    su = 0
    for i, si in enumerate(S[:-2]):
        for j, sj in enumerate(S[i+1:-1]):
            if si == sj:
                continue
            tmps = S[i+j+2:]
            if len(tmps) > j:
                if tmps[j] not in [sj, si]:
                    su -= 1

            tmps2 = [s for s in tmps if s not in [si, sj]]
            su += len(tmps2)
    print(su)


if __name__ == '__main__':
    main()
