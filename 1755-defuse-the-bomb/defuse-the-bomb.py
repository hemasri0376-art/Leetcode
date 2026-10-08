class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        res=[0]*n
        if k==0:
            return res
        if k>0:
            start,end=1,k
        else:
            start,end=n+k,n-1    
        s=0
        for i in range(start,end+1):
            s+=code[i%n]
        for i in range(n):
            res[i]=s
            s-=code[start%n]
            start+=1
            end+=1
            s+=code[end%n]
        return res    