def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # import numpy as np

    # A = np.array(A)
    su = sum(A)
    a = sorted(A, reverse=True)

    tmp = su/M * 0.25

    if a[M-1] < tmp:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
