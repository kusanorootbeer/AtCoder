def main():
    K = int(input())

    i = 0
    lun = 0
    while True:
        i += 1
        ans = check(i)
        if ans != -1:
            lun += 1
        if lun == K:
            print(ans)
            exit()


def check(i):
    li = [int(x) for x in str(i)]
    # num = len(li)
    # print(li)
    for a, b in zip(li[1:], li[:-1]):
        if abs(a-b) <= 1:
            continue
        else:
            return -1
    return i


if __name__ == '__main__':
    main()
