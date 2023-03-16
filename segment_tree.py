#encoding=utf8

"""
线段树
"""


from typing import  *


class sgtree:

# Lazy 线段树模板（区间加，查询区间最小）
    def __init__(self , nums, ):
        n = len(nums)
        self.mn = [0] * (4 * n)
        self.todo = [0] * (4 * n)
        for i in range(n):
            self.update(1,1,n,i + 1,i + 1,nums[i])

    def do(self, o: int, v: int) -> None:
        self.mn[o] += v
        self.todo[o] += v

    def spread(self, o: int) -> None:
        v = self.todo[o]
        if v:
            self.do(o * 2, v)
            self.do(o * 2 + 1, v)
            self.todo[o] = 0

    # 区间 [L,R] 内的数都加上 v   o,l,r=1,1,n
    def update(self, o: int, l: int, r: int, L: int, R: int, v: int) -> None:
        if L <= l and r <= R:
            self.do(o, v)
            return
        self.spread(o)
        m = (l + r) // 2
        if m >= L: self.update(o * 2, l, m, L, R, v)
        if m < R: self.update(o * 2 + 1, m + 1, r, L, R, v)
        self.mn[o] = min(self.mn[o * 2], self.mn[o * 2 + 1])

    # 查询区间 [L,R] 的最小值   o,l,r=1,1,n
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.mn[o]
        self.spread(o)
        m = (l + r) // 2
        if m >= R: return self.query(o * 2, l, m, L, R)
        if m < L: return self.query(o * 2 + 1, m + 1, r, L, R)
        return min(self.query(o * 2, l, m, L, R), self.query(o * 2 + 1, m + 1, r, L, R))

# l = [3,4,1,5,6,7,8,9,3,4]
# sg = sgtree(l)
# print(sg.mn)
# print ( sg.query(1,1,len(l) , 3, len(l)) )
#
# for i ,x in enumerate([1,3,4] , 1):
#     print  ( i ,x )




