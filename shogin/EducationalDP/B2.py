def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    inf = float("inf")
    dp = [inf]*N

    dp[0] = 0

    for i in range(N-1):
        for j in range(1, min(K+1, (N-i))):
            dp[i+j] = min(dp[i+j], abs(H[i+j]-H[i]) + dp[i])
    print(dp[-1])


if __name__ == "__main__":
    main()
