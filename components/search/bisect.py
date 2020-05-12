
def main():
    bisect(ng, ok)


def bisect(ng, ok):
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(arg):
    pass
    return


if __name__ == '__main__':
    main()
