def main():
    import sys
    input = sys.stdin.readline

    X = int(input())

    i = 0
    var = 100
    while True:
        i += 1
        var *= 1.01
        var = int(var)
        if var >= X:
            print(i)
            exit()


if __name__ == "__main__":
    main()
