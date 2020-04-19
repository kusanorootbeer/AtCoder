def main():
    N = int(input())
    A = list(map(int, input().split()))

    import collections

    C = collections.Counter(A)
    m = max(A)
    for i in range(m):
        print(C[i+1])

    for _ in range(N-m):
        print(0)


if __name__ == '__main__':
    main()
