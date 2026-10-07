class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c=0
        for i in range(len(str(num))-k+1):
            s=str(num)[i:i+k]
            if int(s)==0:
                pass
            elif num%int(s)==0:
                c+=1
        return c        