def main():
    import sys
    input = sys.stdin.readline

    N, W = map(int, input().split())
    WV = [list(map(int, input().split())) for i in range(N)]

    V = 10**3*N
    inf = float("inf")
    dp = [[inf] * (V+1) for _ in range(N+1)]

    dp[0][0] = 0
    # i種類目までの荷物を見る
    for i in range(N):
        # その荷物を価値がjになるように持つ
        for j in range(V + 1):
            w, v = WV[i]

            if v <= j:
                # 荷物iを選ぶ場合
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-v] + w)
            # 荷物iを選ばない場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

    # print(dp)
    max_ind = 0
    for j in range(V+1):
        if dp[-1][j] <= W:
            max_ind = j
    print(max_ind)


if __name__ == "__main__":
    main()
