def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    pS = [list(input().split()) for i in range(M)]

    was = [0]*N
    acs = [0]*N

    for p, s in pS:
        q_ind = int(p)-1
        if acs[q_ind] == 0:
            if s == 'AC':
                acs[q_ind] = 1
            else:
                was[q_ind] += 1
    ans_wa = 0
    for i in range(N):
        if acs[i] != 0:
            ans_wa += was[i]

    print(sum(acs), ans_wa)


if __name__ == "__main__":
    main()
