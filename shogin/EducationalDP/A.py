def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    H = list(map(int, input().split()))

    inf = float("inf")
    dp = [inf]*N

    dp[0] = 0
    step1, step2 = inf, inf

    for i in range(1, N):
        step1 = abs(H[i-1]-H[i]) + dp[i-1]
        if i >= 2:
            step2 = abs(H[i-2]-H[i]) + dp[i-2]
        step = min(step1, step2)

        dp[i] = min(dp[i], step)
    print(dp[-1])


if __name__ == "__main__":
    main()
