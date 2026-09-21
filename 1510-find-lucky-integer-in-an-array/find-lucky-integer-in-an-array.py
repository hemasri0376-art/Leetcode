class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        maxi=-1
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]==i:
                maxi=max(maxi,freq[i])
        return maxi         