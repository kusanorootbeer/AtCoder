def main():
    K = int(input())

    su = 0
    for a in range(1, K+1):
        for b in range(1, a+1):
            for c in range(1, b+1):
                tmp = dgcd(a, b, c)
                if a == b and b == c:
                    tmp *= 1
                elif a == b or b == c or a == c:
                    tmp *= 3
                else:
                    tmp *= 6

                su += tmp
    print(su)


def dgcd(a, b, c):
    return gcd(gcd(a, b), c)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    main()
