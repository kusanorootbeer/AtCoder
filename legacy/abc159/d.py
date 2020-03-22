def main():
    import collections

    N = int(input())
    A = list(map(int, input().split()))

    allc = collections.Counter(A)
    allsu = 0
    for pairs in sorted(allc.values(), reverse=True):
        allsu += pairs*(pairs-1)//2

    for a in A:
        num = allc[a]
        print(allsu - (num-1))


if __name__ == '__main__':
    main()
