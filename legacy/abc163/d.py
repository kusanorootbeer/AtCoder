def main():
    N, K = map(int, input().split())
    B = [0]*(N+2-K)
    full = (((N+1)*(N)) // 2)
    for n in range(K, N+2):
        mi = (n*(n-1)) // 2
        ma = full - ((N-n)*(N-n+1)//2)
        B[n-K] = ma-mi+1

    print(sum(B) % (10**9 + 7))


if __name__ == '__main__':
    main()
