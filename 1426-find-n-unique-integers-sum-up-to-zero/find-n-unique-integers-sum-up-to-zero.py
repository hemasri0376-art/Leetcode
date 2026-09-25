class Solution:
    def sumZero(self, n: int) -> list[int]:
        res=[]
        for i in range(1,(n//2)+1):
            res.append(-i)
        if n%2!=0:
            res.append(0)
        for i in range(1,(n//2)+1):
            res.append(i)
        return res            