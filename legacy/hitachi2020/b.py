def main():
    A, B, M = map(int, input().split())
    xyc_list = [0]*M

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    for i in range(M):
        xyc_list[i] = list(map(int, input().split()))

    mini = min(a_list)+min(a_list)
    for x, y, c in xyc_list:
        value = a_list[x-1] + b_list[y-1] - c
        if value < mini:
            mini = value
    print(mini)


if __name__ == '__main__':
    main()
