def main():
    import numpy as np
    K, N = map(int, input().split())
    # As = list(map(int, input().split()))
    As = np.array(list(map(int, input().split())))
    # As[-1] = K-As[-1]

    # print(As[1:]-As[:-1])
    new_A = As[1:]-As[:-1]
    # print(K-As[-1]+As[0])
    a = K-As[-1]+As[0]
    print(sum(new_A) + a - max(max(new_A), a))


if __name__ == '__main__':
    main()
