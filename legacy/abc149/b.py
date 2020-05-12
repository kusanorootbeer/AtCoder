def main():
    import sys
    input = sys.stdin.readline

    A, B, K = map(int, input().split())

    if A >= K:
        print(A-K, B)
    else:
        print(0, max(0, B+A-K))


if __name__ == "__main__":
    main()
