# Cw 1
l1 = [i for i in range(1, 11)]

l2 = l1[5:]
l1 = l1[:5]
print(l1)
print(l2)

# Cw 2
l = l1 + l2
print(l)

l.insert(0, 0)
print(l)

sl = l.copy()
sl.sort(reverse=True)
print(sl)
