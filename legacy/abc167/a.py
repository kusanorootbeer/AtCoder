def main():
    import sys
    input = sys.stdin.readline

    S = list(input().rsplit()[0])
    T = list(input().rsplit()[0])

    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            exit()
    print('Yes')


if __name__ == "__main__":
    main()
