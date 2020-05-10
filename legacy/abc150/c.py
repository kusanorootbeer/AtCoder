def main():
    import sys
    input = sys.stdin.readline
    import numpy as np

    N = int(input())
    P = np.array(list(map(int, input().split())))
    Q = np.array(list(map(int, input().split())))

    import itertools
    X = [i+1 for i in range(N)]
    for i, v in enumerate(itertools.permutations(X)):
        v = np.array(v)
        if (v == P).all():
            p = i
        if (v == Q).all():
            q = i
    print(abs(p-q))


if __name__ == "__main__":
    main()
