#encoding=utf8

from collections import  *
"""
查并集
1.输入是 edges,表示关联的两个元素的索引
2.输出是map,key是元素索引，value是对于的查并集节点索引
"""

from typing import  *
def find(g, x ):
    if g[x] !=x:
        g[x] = find(g,g[x])
    return g[x]
def make_disjoint_set(n, edges: List[List[int]]) -> dict:
    res = {}
    for i in range(1, n+1):
        res[i] = i
    for x, y in edges:
        res[find( res, x)] = find(res, y )
    for i in range(1, n+ 1):
        find(res, i )
    return res


if __name__ == "__main__":
    s = make_disjoint_set(  6, [[1,2], [2,3], [4,5] , [5,6]] )
    #reverse join map
    rs = defaultdict(list)
    for k in s:
        rs[s[k]].append(k)
    print(s ,len(rs) , rs)




