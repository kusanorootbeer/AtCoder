def main():
    import sys
    input = sys.stdin.readline

    N, W = map(int, input().split())
    WV = [list(map(int, input().split())) for i in range(N)]

    dp = [[0] * (W+1) for _ in range(N)]

    # i種類目までの荷物を見る
    for i in range(N):
        # その荷物を重さjになるように持つ
        for j in range(W+1):
            w, v = WV[i]
            num_w = min(1, j//w)        # 荷物は1種につき1個まで
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w*num_w] + v*num_w)
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
