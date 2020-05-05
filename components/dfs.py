# DFS: Depth First Search


def main():
    # s is start point
    # p is path list
    dfs(s, p)



def dfs(s, p):
    # 探索予定スタックに初期値set
    search_list = [s]
    # 探索済みリストの初期化
    visited_list = []

    # 探索予定スタックが空になるまでloop
    while search_list:
        # 探索予定スタックから1つ取り出す(現在地)
        now = search_list.pop()
        # 現在地を探索済みリストに格納
        visited_list.append(now)
        # 現在地から次に行けるポイントを全列挙
        next_step = listup_next()

        # 次に行けるポイントvについての判定
        for v in next_step:
            # vが探索予定スタックに含まれているか
            if judge_s():
                continue
            # vが探索済みリストに含まれているかどうか
            if judge_v():
                continue
            # 上を満たさなければ，探索予定スタックに追加
            search_list.append(v)


if __name__ == '__main__':
    main()
