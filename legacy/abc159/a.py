def main():
    N, M = map(int, input().split())

    sum = N*(N-1)//2
    sum += M*(M-1)//2
    print(sum)


if __name__ == '__main__':
    main()
