N, K = map(int, input().split())
H = list(map(int, input().split()))

Hs = sorted(H)

if K >= N:
    K = N

if K != 0:
    print(sum(Hs[:-K]))
else:
    print(sum(Hs))
