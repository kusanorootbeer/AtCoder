def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    ind = 1
    brick = 0
    for a in A:
        if a == ind:
            ind += 1
        else:
            brick += 1
    if brick == N:
        print(-1)
    else:
        print(brick)


if __name__ == "__main__":
    main()
