def main():
    import sys

    S = list(input())
    N = len(S)

    # c = 0
    # for i in range(0, N-3):
    #     for j in range(i+4, N+1):
    #         num = int(''.join(S[i:j]))
    #         if num % 2019 == 0:
    #             c += 1
    #             print(num)
    # print(c)

    P = 2119
    num = [0] * P
    num[0] = 1
    now, ans = 0, 0
    _10 = 1
    for i in range(N-1, -1, -1):
        now = (now + int(S[i])*_10) % P
        _10 *= 10
        _10 %= P
        ans += num[now]
        num[now] += 1
    print(ans)


if __name__ == "__main__":
    main()
