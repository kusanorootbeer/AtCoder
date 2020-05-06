def main():
    import sys
    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    p = 10**9 + 7
    count = pow(2, n, p)-1

    for i in [a, b]:
        count -= modcomb(n, i, p)

    print(count % (10**9 + 7))


def modcomb(n, r, p):
    x = 1
    y = 1
    for i in range(r):
        x *= n-i
        x %= p
        y *= i+1
        y %= p
    return x*pow(y, p-2, p) % p
    # http://nagoyacoder.web.fc2.com/topcoder/topcoder_cpp4.html


if __name__ == "__main__":
    main()
