def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for i in range(Q)]
    score = 0

    def dfs(l, **kwargs):
        N = kwargs['N']
        M = kwargs['M']
        ABCD = kwargs['ABCD']

        # 末端まで探索したか判定
        if judge_end(l, N=N):
            nonlocal score
            tmp_score = calc_score(l, ABCD=ABCD)
            score = max(tmp_score, score)
            return
        else:
            # 現時点から選べる選択肢の列挙と探索
            nexts = listup_next(l[-1], M=M)
            for x in nexts:
                dfs(l+[x], N=N, M=M, ABCD=ABCD)

    def judge_end(l, **kwargs):
        N = kwargs['N']
        return len(l) == N

    def calc_score(l, **kwargs):
        ABCD = kwargs['ABCD']
        s = 0
        for a, b, c, d in ABCD:
            if l[b-1] - l[a-1] == c:
                s += d
        return s

    def listup_next(now, **kwargs):
        m = now
        M = kwargs['M']
        return range(m, M+1)

    for i in range(1, M+1):
        dfs([i], N=N, M=M, ABCD=ABCD)
    print(score)


if __name__ == "__main__":
    main()
