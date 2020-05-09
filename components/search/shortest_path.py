# shortest_path

import numpy as np
from scipy.sparse import csgraph
from scipy.sparse import csr_matrix


def main():
    # Arr : 隣接行列
    # sample
    Arr = np.array([[0, 1, 2, 0],
                    [0, 0, 0, 1],
                    [3, 0, 0, 3],
                    [0, 0, 0, 0]])

    # 全点対最短経路
    d = csgraph.shortest_path(Arr)
    print(d)
    # 単一始点最短経路
    start = 0
    d = csgraph.shortest_path(Arr, indices=start)
    start2 = 1
    d = csgraph.shortest_path(Arr, indices=[start, start2])

    # 最短経路獲得
    d, p = csgraph.shortest_path(Arr, return_predecessors=True)
    start = 0
    end = 3
    root = get_path(start, end, p)

    # その他引数について
    '''
    directed: bool: デフォルトはTrue
    unweighted: bool: デフォルトはFalse, Trueだとすべての重みを1にする
    '''

    # optional
    '''
    method選択によって高速化が可能
        dijkstraを使いたいときは, 引数limitが必要になる
    numpy arrayじゃなくてcsr_matrixの方が高速らしい
    '''
    N = 5
    cost = [1, 2, 1, 3, 3]
    starts = [0, 0, 1, 2, 2]
    nexts = [1, 2, 3, 0, 3]
    csr = csr_matrix((cost, (starts, nexts)), shape=(N, N))
    print(csr)


def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])


def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]


if __name__ == '__main__':
    main()
