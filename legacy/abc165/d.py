def main():
    import sys
    input = sys.stdin.readline

    A, B, N = map(int, input().split())

    x = min(B-1, N)
    print(int(A*x/B)-A*int(x/B))


if __name__ == "__main__":
    main()
