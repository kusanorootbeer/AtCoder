def main():
    S = input()

    for i, s in enumerate(S):
        if i % 2 == 0:
            if s == 'h':
                continue
            else:
                print('No')
                exit()
        else:
            if s == 'i':
                continue
            else:
                print('No')
                exit()
    if i % 2 == 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
