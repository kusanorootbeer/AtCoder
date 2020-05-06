def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    s = []
    while True:
        n = N % K
        N //= K
        if N == 0 and n == 0:
            break
        s.append(n)
    print(len(s))


if __name__ == "__main__":
    main()
