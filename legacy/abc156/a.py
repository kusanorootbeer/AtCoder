def main():
    import sys
    input = sys.stdin.readline

    N, R = map(int, input().split())
    if N < 10:
        K = N
    else:
        K = 10
    print(R+100*(10-K))


if __name__ == "__main__":
    main()
