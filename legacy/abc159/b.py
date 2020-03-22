def main():
    S = list(input())
    N = len(S)

    kaibun_check(S)

    S1 = S[0:(N-1)//2]
    kaibun_check(S1)

    S2 = S[(N+3)//2:-1]
    kaibun_check(S2)

    print('Yes')


def kaibun_check(L):
    L_ = list(L.__reversed__())
    for s, s_ in zip(L, L_):
        if s != s_:
            print('No')
            exit()


if __name__ == '__main__':
    main()
