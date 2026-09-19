class Solution:
    def minimumSum(self, num: int) -> int:
        res=[]
        for i in range(4):
            res.append(num%10)
            num=num//10
        res.sort()
        f=res[0]*10+res[2]
        l=res[1]*10+res[3]
        return f+l