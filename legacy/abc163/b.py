def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    su = sum(A)
    if su > N:
        print(-1)
    else:
        print(N-su)


if __name__ == '__main__':
    main()
