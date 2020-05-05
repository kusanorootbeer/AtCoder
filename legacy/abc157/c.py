# import numpy as np
def main():
    N, M = map(int, input().split())
    s, c = [], []
    for i in range(M):
        si, ci = map(int, input().split())
        s.append(si)
        c.append(ci)

    res = ['']*N
    for si, ci in zip(s, c):
        if res[si-1] == '':
            res[si-1] = str(ci)
        elif res[si-1] != str(ci):
            print(-1)
            exit()

    if res[0] == '0':
        if N == 1:
            print(0)
            exit()
        else:
            print(-1)
            exit()
    elif res[0] == '':
        res[0] = str(1)

    for i in range(N):
        if res[i] == '':
            res[i] = str(0)
    if M == 0 and N == 1:
        print(0)
        exit()
    print(int("".join(res)))


if __name__ == "__main__":
    main()
