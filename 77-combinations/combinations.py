class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        a=[i for i in range(1,n+1)]
        res=[]
        for i in combinations(a,k):
            res.append(i)
        return res    