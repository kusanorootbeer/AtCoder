N = int(input().split()[0])
A = list(map(int, input().split()))

if len(A) == len(set(A)):
    print('YES')
else:
    print("NO")
