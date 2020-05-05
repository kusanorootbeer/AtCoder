import numpy as np

N = input().split()
A = list(map(int, input().split()))

A = np.array(A)

B = A[np.where(A % 2 == 0, True, False)]
C = np.where(B % 3 == 0, True, False) + np.where(B % 5 == 0, True, False)

if C.all():
    print("APPROVED")
else:
    print("DENIED")
