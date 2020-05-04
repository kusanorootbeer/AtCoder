# DFS: Depth First Search


def main():
    score = 0
    for i in range(1, M+1):
        dfs([i])
    print(score)


def dfs(l, **kwargs):
    # 末端まで探索したか判定
    if judge_end():
        global score
        # 経路の評価
        tmp_score = calc_score()
        score = max(tmp_score, score)
        return
    else:
        # 現時点から選べる選択肢の列挙と探索
        for x in listup_next():
            dfs(l+[x])


def judge_end(l, **kwargs):
    pass
    return


def calc_score(l, **kwargs):
    pass
    return


def listup_next(l, **kwargs):
    pass
    return


if __name__ == '__main__':
    main()
