class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_arr=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for char,count in sorted_arr:
            res.append(char*count)    
        return "".join(res)        