S, T = input().split()
A, B = map(int, input().split())
U = input().split()[0]


if U == S:
    A = A-1
else:
    B = B-1
print(A, B)
