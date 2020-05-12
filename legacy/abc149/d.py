def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    RSP = list(map(int, input().split()))
    T = list(input().rsplit()[0])

    win_hand = ['s', 'p', 'r']

    ans = 0
    hand = [0]*N
    for i in range(N):
        for j in range(3):
            if T[i] == win_hand[j]:
                if i >= K:
                    if T[i] == T[i-K] and T[i] == hand[i-K]:
                        continue
                hand[i] = win_hand[j]
                ans += RSP[j]
    print(ans)


if __name__ == "__main__":
    main()
