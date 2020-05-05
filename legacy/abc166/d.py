def main():
    import sys
    input = sys.stdin.readline

    X = int(input())
    for a in range(-200, 200):
        a5 = a**5
        b5 = a5-X
        for b in range(-200, 200):
            if b**5 == b5:
                print(a, b)
                exit()


if __name__ == "__main__":
    main()
