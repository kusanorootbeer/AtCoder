def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [list(map(int, input().split())) for i in range(N)]
    S = list(input().rsplit()[0])


if __name__ == "__main__":
    main()
