def main():
    import sys
    input = sys.stdin.readline

    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)
    want = N*M - total
    if want > K:
        print(-1)
        exit()
    print(max(0, want))


if __name__ == "__main__":
    main()
