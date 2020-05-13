def main():
    import sys
    input = sys.stdin.readline
    from fractions import gcd

    A, B = map(int, input().split())

    print((A*B)//gcd(A, B))


if __name__ == "__main__":
    main()
