class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened,close=0,0
        for i in s:
            if i=='(':
                opened+=1
            elif opened:
                opened-=1    
            else:
                close+=1
        return close+opened           