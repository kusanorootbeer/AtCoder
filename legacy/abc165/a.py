def main():
    import sys
    input = sys.stdin.readline

    K = int(input())
    A, B = map(int, input().split())

    x = A//K

    y = B//K

    for i in range(A, B+1):
        if i % K == 0:
            print('OK')
            exit()
    if A == B and A % K == 0:
        print('OK')
        exit()
    print('NG')


if __name__ == "__main__":
    main()
