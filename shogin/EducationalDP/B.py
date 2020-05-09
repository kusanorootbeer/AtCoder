def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    inf = float("inf")
    dp = [inf]*N

    dp[0] = 0
    steps = [inf] * K

    for i in range(1, N):
        steps = [inf] * K
        for j in range(1, min(i, K) + 1):
            steps[j-1] = abs(H[i-j]-H[i]) + dp[i-j]
        step = min(steps)

        dp[i] = min(dp[i], step)
    print(dp[-1])


if __name__ == "__main__":
    main()
