H, A = map(int, input().split())


a = H//A
a = a+1
if H % A == 0:
    a = a-1
print(a)
