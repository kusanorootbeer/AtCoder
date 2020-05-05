import numpy as np
import collections

N = int(input().split()[0])
A = []
for i in range(N):
    A.append(input().split()[0])

C = collections.Counter(A)
c = C.most_common()
m = c[0][1]
x = []
for c, n in c:
    if n == m:
        x.append(c)
    else:
        break
x = sorted(x)
for i in x:
    print(i)
