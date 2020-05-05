import collections
N = int(input())

num = 0

li = [i+1 for i in range(N)]

l4 = list(map(lambda x: str(x)[0]+str(x)[-1], li))
ll = set(l4)
l5 = list(map(lambda x: str(x)[-1]+str(x)[0], li))
c4 = collections.Counter(l4)
c5 = collections.Counter(l5)

for l in ll:
    num += c4[l] * c5[l]
print(num)

