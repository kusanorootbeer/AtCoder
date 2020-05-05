def main():
    import sys
    input = sys.stdin.readline
    import numpy as np
    from collections import Counter
    N = int(input())
    A = np.array(list(map(int, input().split())))

    count = 0

    tmp = np.arange(N)
    X = A-tmp
    Y = A+tmp

    XX = Counter(list(X))
    YY = Counter(list(Y))

    count = 0
    for number, c in XX.items():
        count += YY[-number] * c
    print(count)


if __name__ == "__main__":
    main()
