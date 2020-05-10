def main():
    import sys
    input = sys.stdin.readline
    import numpy as np

    N, M, X = map(int, input().split())
    CA = np.array([list(map(int, input().split())) for i in range(N)])

    Z = [list(format(i, '0{}b'.format(N))) for i in range(2**N)]

    cost = np.inf
    for z in Z[1:]:
        ind = np.array(z) == '1'
        ca = np.sum(CA[np.where(ind)], axis=0)
        if np.sum(ca[1:] >= X) == M:
            cost = min(cost, ca[0])
    if cost == np.inf:
        cost = (-1)
    print(cost)


if __name__ == "__main__":
    main()
