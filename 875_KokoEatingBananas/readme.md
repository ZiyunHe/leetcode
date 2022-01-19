python syntax b if a > 10 else c

wrong case:
[312884470]
968709470
# 说明了 start should be 1 not 0


这道题求的是min。所以这样写
    m = (s+e) // 2
    hours = self.eats(piles, h, m)
    if hours <= h:
        e = m
    elif hours > h:
        s = m + 1

如果求的是max。这样写。 举例子【s4, e5] m=s+e+1=5 而不能等于4
    m = (s+e+1) // 2
    hours = self.eats(piles, h, m)
    print(s, e, m)
    if hours >= h:
        s = m
    elif hours < h:
        e = m - 1


(p-1) // k + 1
p = 12, k = 4, 12/4 = 3
p = 13, k = 4, 13/4+1 = 4
p = 14, k = 4, 14/4+1 = 4
p = 15, k = 4, 15/4+1 = 4
p = 16, k = 4, 16/4 = 4