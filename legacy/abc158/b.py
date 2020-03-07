def main():

    N, A, B = map(int, input().split())

    # blue = ['b']*A
    # red = ['r']*B
    # l = []
    # while len(l) <= N:
    #     l.extend(blue)
    #     l.extend(red)
    # print(l[:N].count('b'))

    # c = 0
    # len = 0
    # while len <= N-A:
    #     len += A+B
    #     c += A
    # c += N-len
    # print(c)

    loops = N // (A+B)
    c = A*loops
    c += min(A, N % (A+B))
    print(c)


if __name__ == '__main__':
    main()
