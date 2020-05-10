def main():
    import sys
    input = sys.stdin.readline

    A, B, C, K = map(int, input().split())

    ans = 0
    k = 0
    ans += min(A, K-k)
    k += min(A, K-k)
    k += min(B, K-k)
    ans -= K-k

    print(ans)


if __name__ == "__main__":
    main()
