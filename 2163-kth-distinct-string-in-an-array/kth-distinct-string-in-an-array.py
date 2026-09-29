class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq={}
        res=[]
        for i in arr:
            freq[i]=freq.get(i,0)+1
        distinct_count = 0
        for i in arr:
            if freq[i] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return i
        return ""    
