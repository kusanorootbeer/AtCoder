A, B, C = input().split()

if A == B:
    if A == C:
        print("No")
        exit()
    else:
        print("Yes")
        exit()
elif A == C:
    if A != B:
        print("Yes")
        exit()
elif B == C:
    print("Yes")
    exit()
else:
    print("No")
    exit()
