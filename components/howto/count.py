from collections import Counter

# sample
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = Counter(l)

# get number of 'a'
c['a']    # 4
c['d']   # 0

# for get list
c.keys()    # ['a', 'b', 'c']
c.values()  # [4, 1, 2]
c.items()   # [('a', 4), ('b', 1), ('c', 2)]
c.most_common()  # [('a', 4), ('c', 2), ('b', 1)]

values, counts = zip(*c.most_common())
# ('a', 'c', 'b'), (4, 2, 1)
