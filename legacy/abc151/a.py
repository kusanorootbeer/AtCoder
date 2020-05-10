def main():
    import sys
    input = sys.stdin.readline

    C = list(input().rsplit()[0])[0]

    print(chr(ord(C)+1))


if __name__ == "__main__":
    main()
