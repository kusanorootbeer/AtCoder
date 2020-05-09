def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    ABC = [list(map(int, input().split())) for i in range(N)]

    dp = [[0]*3 for i in range(N)]
    dp[0] = ABC[0]

    for i in range(N-1):
        a, b, c = ABC[i+1]

        dp[i+1][0] = a + max(dp[i][1], dp[i][2])
        dp[i+1][1] = b + max(dp[i][0], dp[i][2])
        dp[i+1][2] = c + max(dp[i][0], dp[i][1])

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
