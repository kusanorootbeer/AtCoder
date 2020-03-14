def main():
    import sys
    # import math
    # import decimal
    input = sys.stdin.readline
    a, b, c = map(int, input().split())

    if a+b < c:
        if (c-a-b)**2 > 4*a*b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()
