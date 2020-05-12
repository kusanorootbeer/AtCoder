import math


def main():
    import sys
    input = sys.stdin.readline
    from fractions import gcd

    X = int(input())

    for x in range(X, 10**6):
        if prime_judge(x):
            print(x)
            exit()


def prime_judge(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
