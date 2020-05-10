def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = list(input().rsplit()[0])

    ans = 0
    for i in range(len(S)):
        s = "".join(S[i:i+3])
        if s == 'ABC':
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
