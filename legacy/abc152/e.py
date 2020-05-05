from fractions import gcd

N = int(input())

A = list(map(int, input().split()))

l = A[0]
for a in A:
    l = (l * a) // gcd(l, a)
num = 0
for a in A:
    num += l//a
print(num % (10**9 + 7))
