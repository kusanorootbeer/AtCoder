def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())

    d = [0]*K
    A = [0]*K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))

    have = []
    for a in A:
        have[len(have):] = set(a)
    print(N - len(set(have)))


if __name__ == "__main__":
    main()
