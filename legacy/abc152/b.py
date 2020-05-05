a, b = map(int, input().split())

if a >= b:
    less = b
    big = a
else:
    less = a
    big = b

st = str(less)
out = ""
for i in range(big):
    out += st
print(out)
