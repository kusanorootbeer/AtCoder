import sys

N = int(input())
ll = []
ll = list(map(int, input().split()))

num = 0
mi = ll[0]
for i in range(N):
    a = ll[i]
    if mi >= a:
        mi = a
        num += 1

print(num)
