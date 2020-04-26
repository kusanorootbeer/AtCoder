def main():
    import sys
    input = sys.stdin.readline

    S, W = map(int, input().split())
    if S > W:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    main()
