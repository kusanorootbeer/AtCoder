def main():
    # import sys
    # input = sys.stdin.readline

    N = int(input())
    S = [0]*N
    for i in range(N):
        S[i] = input()

    print(len(set(S)))


if __name__ == "__main__":
    main()
