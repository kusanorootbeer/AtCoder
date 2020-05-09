def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    ABC = [list(map(int, input().split())) for i in range(N)]

    dp = [[0]*3 for i in range(N)]
    dp[0] = ABC[0]

    for i in range(1, N):
        a, b, c = ABC[i]

        dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
