def main():
    import sys
    input = sys.stdin.readline
    import numpy as np
    from scipy.sparse import csr_matrix

    N, M = map(int, input().split())
    H = np.array(list(map(int, input().split())))

    AB = [[] for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        AB[a].append(b)
        AB[b].append(a)
    count = 0
    for i, ab in enumerate(AB):
        ind = list(set(ab))
        if ind == []:
            count += 1
            continue
        if np.max(H[ind]) < H[i]:
            count += 1
    print(count)

    # AB = np.array([list(map(int, input().split())) for i in range(M)])-1

    # ab0 = list(AB[:, 0])
    # ab1 = list(AB[:, 1])
    # csr = csr_matrix(
    #     ([1]*(2*M), (ab0+ab1, ab1+ab0)), shape=(N, N)).toarray()

    # count = 0
    # for i, indices in enumerate(csr):
    #     if (indices == 0).all():
    #         count += 1
    #         continue
    #     if np.max(H[indices != 0]) < H[i]:
    #         count += 1

    # print(count)


if __name__ == "__main__":
    main()
