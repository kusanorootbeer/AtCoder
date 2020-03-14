def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())

    m = H*W // 2 + (H*W) % 2

    if H == 1 or W == 1:
        print(1)
    else:
        print(m)


if __name__ == '__main__':
    main()
