def main():
    N, K = map(int, input().split())

    tmp = N % K
    print(min(tmp, abs(K-tmp)))


if __name__ == '__main__':
    main()
