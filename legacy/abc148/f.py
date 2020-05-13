def main():
    import sys
    input = sys.stdin.readline
    from scipy.sparse import csgraph, csr_matrix
    import numpy as np

    N, u, v = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N-1)]

    u = u-1
    v = v-1

    cost = [1]*(N-1)
    starts = [0]*(N-1)
    nexts = [0]*(N-1)
    for i, ab in enumerate(AB):
        starts[i] = ab[0]-1
        nexts[i] = ab[1]-1

    csr = csr_matrix((cost+cost, (starts+nexts, nexts+starts)), shape=(N, N))
    dd = csgraph.shortest_path(csr)
    d = np.array([dd[u], dd[v]])
    # print(d)

    cand1 = (d[0]+1 == d[1]) + (d[0] == 0)
    cand2 = (d[0] == d[1])
    ans = 0
    # for a, b in zip(d[0][cand], d[1][cand]):

    # print(cand1)
    # print(cand2)
    # print(d[0][cand1])
    # print(d[1][cand2])
    if d[0][v] == 1:
        ans = 0
    else:
        ans = int(max(d[0][cand1]))
        try:
            ans = max(ans, int(min(d[1][cand2])))
        except:
            pass
    print(ans)


if __name__ == "__main__":
    main()
