def main():
    X = int(input())

    five_hund = X // 500
    Q = X % 500
    five = Q // 5
    print(five_hund*1000 + five*5)



if __name__ == '__main__':
    main()
