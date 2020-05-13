def main():
    import sys
    input = sys.stdin.readline

    A = int(input())
    B = int(input())

    ans = [1, 2, 3]
    for a in ans:
        if a != A and a != B:
            print(a)


if __name__ == "__main__":
    main()
