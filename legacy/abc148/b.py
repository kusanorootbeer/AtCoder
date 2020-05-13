def main():
    # import sys
    # input = sys.stdin.readline

    N = int(input())
    S, T = map(list, input().split())

    ans = ''
    for s, t in zip(S, T):
        ans += s+t
    print(ans)


if __name__ == "__main__":
    main()
