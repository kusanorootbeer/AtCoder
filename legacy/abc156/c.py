def main():
    import sys
    input = sys.stdin.readline
    import numpy as np

    N = int(input())
    X = list(map(int, input().split()))

    X_arr = np.array(X)
    mean = X_arr.mean()

    x1 = int(mean)
    x2 = int(mean)+1

    v1 = np.sum((X_arr-x1)**2)
    v2 = np.sum((X_arr-x2)**2)
    print(min(v1, v2))


if __name__ == "__main__":
    main()
