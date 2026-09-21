class Solution:
    def sortString(self, s: str) -> str:
        s=sorted(s)
        freq={}
        res=[]
        for i in s:
            freq[i]=freq.get(i,0)+1
        while len(res)<len(s) :   
            for i in freq:
                if freq[i]>0:
                    res.append(i)
                    freq[i]-=1
            for i in reversed(freq):
                if freq[i]>0:
                    res.append(i)  
                    freq[i]-=1  
        return "".join(res)    
